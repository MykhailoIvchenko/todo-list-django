from django.urls import path

from todos.views import IndexView, TagListView, TagCreateView, TagUpdateView, TagDeleteView, AppUserUpdateView, \
    AppUserDetailView, AppUserDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView

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
        "profile/", AppUserDetailView.as_view(), name="app_user-detail"
    ),
    path(
        "profile/update/",
        AppUserUpdateView.as_view(),
        name="app_user-update",
    ),
    path(
        "profile/delete/",
        AppUserDeleteView.as_view(),
        name="app_user-delete",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todos"
