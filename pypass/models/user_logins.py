from django.db import models
from django.contrib.auth.models import User
from pypass.models.brand_icons import BrandIcons


class UserSavedLogins(models.Model):
    id_user_logins = models.BigAutoField(
        primary_key=True,

    )
    sitename = models.CharField(
        max_length=50
    )
    brand_icon = models.ForeignKey(
        BrandIcons,
        on_delete=models.CASCADE
    )
    username = models.CharField(
        max_length=50,
        blank=True
    )
    email = models.CharField(
        max_length=50,
        blank=True
    )
    password = models.CharField(
        max_length=255,
        blank=True
    )
    notes = models.CharField(
        max_length=140,
        blank=True
    )
    is_fav = models.BooleanField(
        default=False
    )
    app_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
