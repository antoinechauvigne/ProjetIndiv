from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Communaute, Post


# Create your views here.
@login_required
def communautes(request):
    """ Afficher les communautes et le statut d'abonnement """

    # Nous sélectionnons toutes les instances de la classe Communaute
    list_communautes = get_list_or_404(Communaute)
    ma_communaute = Communaute.objects.filter(abonnes__id=2)

    return render(request, 'communitymanager/communautes.html', locals())

@login_required
def communaute(request, communaute_id):
    """ Afficher les posts d'une communaute """

    posts = Post.objects.filter(communaute__id=communaute_id)

    return render(request, 'communitymanager/communaute.html', locals())