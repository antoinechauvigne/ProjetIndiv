from django import forms
from .models import Commentaire, Post



class CommentaireForm(forms.Form):
    #Pour que la case s'affiche sur plusieurs lignes
    contenu = forms.CharField(widget=forms.Textarea, label='Votre Commentaire')



class NouveauPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('auteur', 'date_creation')

    def clean(self):
        """
        Un événement doit contenir une date et une date ne peut pas ne pas être associée à un événement
        """
        cleaned_data = super(NouveauPostForm, self).clean()
        evenementiel = cleaned_data['evenementiel']
        date_evenement = cleaned_data['date_evenement']

        if (evenementiel and date_evenement == None):
                raise forms.ValidationError('Précisez la date de votre événement')
        if (not evenementiel and date_evenement != None):
                raise forms.ValidationError('Vous semblez vouloir créer un événement, veuillez cocher la case correspondante')

        return cleaned_data

