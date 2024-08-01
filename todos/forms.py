from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from todos.models import AppUser, Task, Tag


class AppUserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name")


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"
