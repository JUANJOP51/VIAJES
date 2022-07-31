from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.TextField(max_length=800)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



# Create your models here.
