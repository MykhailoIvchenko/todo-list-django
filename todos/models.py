from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class AppUser(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("todos:user-detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="user")

    class Meta:
        ordering = ['is_completed', '-created_at']

    def __str__(self):
        return f"{self.content}"
