from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from todos.models import Task, Tag, AppUser


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    context_object_name = "tasks_list"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).select_related("tags")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todos/tags_list.html"
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todos:tags-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todos:tags-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todos:tags-list")


class AppUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = AppUser
    template_name = "todos/app_user_detail.html"
    context_object_name = 'app_user'


class AppUserDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = AppUser
    success_url = reverse_lazy("todos:index")
    template_name = "todos/app_user_confirm_delete.html"


