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
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=False,
    )
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "datetime-local", "class": "form-control"}),
        required=False
        )
    is_completed = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_completed", "tags"]
