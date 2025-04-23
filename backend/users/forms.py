from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Introduce un email válido.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'phone',
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'phone',
        )
