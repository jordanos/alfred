from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_OPTIONS = [("USER", "USER"), ("ADMIN", "ADMIN")]


class User(AbstractUser):
    role = models.CharField(
        max_length=25, default=ROLE_OPTIONS[0][0], choices=ROLE_OPTIONS
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.email} "
