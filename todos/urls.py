from django.urls import path

from todos.views import (
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    AppUserUpdateView,
    AppUserDetailView,
    AppUserDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleStatusView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
            "tags/",
            TagListView.as_view(),
            name="tags-list",
        ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "profile/<int:pk>", AppUserDetailView.as_view(), name="app_user-detail"
    ),
    path(
        "profile/<int:pk>/update/",
        AppUserUpdateView.as_view(),
        name="app_user-update",
    ),
    path(
        "profile/<int:pk>/delete/",
        AppUserDeleteView.as_view(),
        name="app_user-delete",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", TaskToggleStatusView.as_view(), name="task-toggle-status"),
]

app_name = "todos"
