from django.conf import settings
from django.db import models
from videos.models import Video


class Comment(models.Model):
    video = models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}: {self.content[:20]}"
