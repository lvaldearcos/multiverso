from django.db import models


# Create your models here.

class Personaje(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.TextField()
    nombre = models.TextField()
    poderes = models.TextField()
    origen = models.TextField()

    def __str__(self):
        return self.nombre
