from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "date_of_birth",
            "first_name",
            "last_name",
        )

    def clean_password_confirm(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords don't match")
        return password_confirm

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
            "date_of_birth",
            "first_name",
            "last_name",
            "is_active",
            "is_admin",
        )

    def clean_password(self):
        return self.initial["password"]
