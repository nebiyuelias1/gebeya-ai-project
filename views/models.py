from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class View(models.Model):
    # The text content of the View.
    content = models.CharField(max_length=560, null=False, blank=False)

    # The user that created the View.
    user = models.ForeignKey(User, related_name='+', null=True, blank=True, on_delete=models.SET_NULL)

    # The time the view was posted.
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
