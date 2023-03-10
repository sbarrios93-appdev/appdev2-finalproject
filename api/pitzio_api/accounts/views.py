from typing import cast

from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from .models import CustomUser
from .serializers import (
    LoginSerializer,
    PasswordChangeSerializer,
    RegistrationSerializer,
    UserSerializer,
)

# Create your views here.


class UserListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class RegistrationView(GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        if "email" not in request.data or "password" not in request.data:
            return Response(
                {"message": "Credentials missing"}, status=status.HTTP_400_BAD_REQUEST
            )
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            user = cast(CustomUser, user)
            login(request, user)
            return Response(
                {
                    "message": "Login Success",
                    "id": user.id,
                    **user.get_refresh_tokens(),
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response(
            {"message": "Successfully Logged out"}, status=status.HTTP_200_OK
        )


class ChangePasswordView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = PasswordChangeSerializer(
            context={"request": request}, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserView(GenericAPIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
