from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'middle_name', 'email', 'password1', 'password2',)
