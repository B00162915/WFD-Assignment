from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    roleChoices = (
        ("manager", "Manager"),
        ("coach", "Coach"),
        ("finance", "Finance"),
        ("player", "Player"),
    )
    
    role = models.CharField(choices = roleChoices)

    def __str__(self):
        return f"{self.username} ({self.role})"