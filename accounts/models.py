from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    edad = models.IntegerField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
