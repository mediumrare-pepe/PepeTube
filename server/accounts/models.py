from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Profile information for a :class:`django.contrib.auth.models.User`."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.user.username} profile"
