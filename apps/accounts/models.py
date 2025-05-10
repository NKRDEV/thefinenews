from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    # Add any custom fields here
    pass


class NewsOwnerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # Use settings.AUTH_USER_MODEL directly
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
