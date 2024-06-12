from django.contrib.auth.models import AbstractUser
from django.core.validators import (  # RegexValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.db import models

# Create your models here.


class Users(AbstractUser):
    realname = models.CharField("User's real name", max_length=50)
    username = models.CharField(
        "ID for user used in website",
        max_length=255,
        null=False,
        unique=True,
        editable=False,
    )
    password = models.CharField("Hashed password", max_length=255, null=False)
    phone_number = models.CharField(
        "Phone Number for Company",
        validators=(MaxLengthValidator(11), MinLengthValidator(10)),
        max_length=20,
    )
