from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from todos.models import AppUser


class AppUserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name")

