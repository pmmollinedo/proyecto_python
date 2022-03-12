from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    avatar = models.CharField(
        max_length=50,
        default='default_profile_1.svg'
    )

    status = models.CharField(
        max_length=50,
        default='Chilling'
    )

    def __str__(self):
        return f"Profile [{self.user}]"
