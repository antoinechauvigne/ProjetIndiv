from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Communaute(models.Model):
    nom = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    class Meta:
        verbose_name = "communaute"
        ordering = ['nom']

    def __str__(self):
        return self.nom