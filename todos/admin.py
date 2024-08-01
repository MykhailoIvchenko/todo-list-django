from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from todos.models import AppUser, Task, Tag


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("user",)


admin.site.register(Tag)

