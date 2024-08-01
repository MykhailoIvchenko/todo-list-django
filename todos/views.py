from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from todos.models import Task


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = "tasks_list"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).select_related("tags")
