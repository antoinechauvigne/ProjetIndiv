from django import forms
from .models import Commentaire



class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)  # on veut utiliser tous les champs de la classe Commenature
    #Pour que la case s'affiche sur plusieurs lignes
    #contenu = forms.CharField(widget=forms.Textarea)
