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

    def clean(self):
        """
        Un événement doit contenir une date
        """
        cleaned_data = super(NouveauPostForm, self).clean()
        evenementiel = cleaned_data['evenementiel']
        date_evenement = cleaned_data['date_evenement']

        if evenementiel:
            if date_evenement == "<null>":
                print('problem')
                raise forms.ValidationError('Précisez la date de votre événement')
        return cleaned_data

