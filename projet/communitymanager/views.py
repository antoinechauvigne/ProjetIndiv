from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Communaute

# Create your views here.
@login_required
def communautes(request):
    """ Afficher les communautes et le statut d'abonnement """

    # Nous sélectionnons toutes les instances de la classe Communaute
    list_communautes = get_list_or_404(Communaute)

    return render(request, 'communitymanager/communautes.html', locals())