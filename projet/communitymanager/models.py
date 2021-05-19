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


class Priorite(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Post(models.Model):
    titre = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    date_creation = models.DateField()
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField()
    date_evenement = models.DateField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    date_creation = models.DateField()
    contenu = models.CharField(max_length=2000)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.contenu



