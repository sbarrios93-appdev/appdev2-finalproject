# Create your views here.
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import (
    ChangePasswordView,
    CurrentUserView,
    LoginView,
    LogoutView,
    RegistrationView,
    UserListView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("register", RegistrationView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("change-password", ChangePasswordView.as_view(), name="change-password"),
    path(
        "token-refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("user", CurrentUserView.as_view(), name="user"),
]
