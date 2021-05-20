from django import forms
from .models import Commentaire, Post



class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)  # on veut utiliser tous les champs de la classe Commenature
    #Pour que la case s'affiche sur plusieurs lignes
    #contenu = forms.CharField(widget=forms.Textarea)


class NouveauPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur',)
