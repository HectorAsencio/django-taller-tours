from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class Usuario(AbstractUser):
    rut = models.CharField(max_length=16)


class Tour(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField(max_length=500)
    foto = models.ImageField(default='tours/default.jpg', upload_to='tours')
    requisitos = models.TextField(max_length=500, default='Sin requisitos adicionales.')
    dias = models.SmallIntegerField(null=True, blank=True)
    precio = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def save(self):
        super().save()
        img = Image.open(self.foto.path)
        if (img.height > 480 or img.width > 640):
            output_size = (640, 640)
            img.thumbnail(output_size)
            img.save(self.foto.path)
