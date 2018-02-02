from django.db import models

# Create your models here.

class Continent(models.Model):
    color = models.CharField(max_length = 15, unique=True)
    name = models.CharField(max_length = 15, unique=True)
    traslation = models.CharField(max_length = 15, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Continents"
        ordering = ("name",)
