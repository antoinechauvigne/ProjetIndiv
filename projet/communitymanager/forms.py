from django import forms
from .models import Post
from django.forms import widgets

class CommentaireForm(forms.Form):
    """Formulaire d'ajout de commentaire à un post"""

    # Pour que la case s'affiche sur plusieurs lignes
    contenu = forms.CharField(widget=forms.Textarea, label='Votre Commentaire')


class NouveauPostForm(forms.ModelForm):
    """Formulaire de création et de modification d'un post"""

    class Meta:
        model = Post
        exclude = ('auteur', 'date_creation')
        widgets = {
            'date_evenement': widgets.SelectDateWidget(),
        }

    def clean(self):
        """Un événement doit contenir une date et une date ne peut pas ne pas être associée à un événement"""
        cleaned_data = super(NouveauPostForm, self).clean()
        if'date_evenement' in cleaned_data.keys():
            evenementiel = cleaned_data['evenementiel']
            date_evenement = cleaned_data['date_evenement']

            if (evenementiel and date_evenement == None):
                raise forms.ValidationError('Précisez la date de votre événement')
            if (not evenementiel and date_evenement != None):
                raise forms.ValidationError(
                    'Vous semblez vouloir créer un événement, veuillez cocher la case correspondante')

        return cleaned_data
