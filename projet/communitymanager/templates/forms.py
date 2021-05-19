from django import forms
from projet.communitymanager.models import Commentaire


class CommentaireForm(forms.Form):
    #Pour que la case s'affiche sur plusieurs lignes
    contenu = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Commentaire
        fields = '__all__'  # on veut utiliser tous les champs de la classe Article