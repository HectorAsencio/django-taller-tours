from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    rut = models.CharField(max_length=10)


class Tour(models.Model):
    nombre = models.CharField(max_length=64)
    dias = models.SmallIntegerField(null=True, blank=True)
    precio = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre
