from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE = (
        ("management", "Management"),
        ("sale", "Sale"),
        ("support", "Support"),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE,
        blank=True,
    )
