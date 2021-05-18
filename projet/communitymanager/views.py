from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Communaute, Post


# Create your views here.
@login_required
def communautes(request):
    """ Afficher les communautes et le statut d'abonnement """

    # Nous sélectionnons toutes les instances de la classe Communaute
    list_communautes = get_list_or_404(Communaute)
    for communaute in list_communautes:
        #print(communaute.abonnes.all())

        je_suis_abonne = False
        if request.user in communaute.abonnes.all():
            je_suis_abonne = True
        communaute.user_abonne = je_suis_abonne

        #print(communaute.user_abonne)
    #ma_communaute = Communaute.objects.filter(abonnes__id=request.user.id)

    return render(request, 'communitymanager/communautes.html', locals())

@login_required
def communaute(request, communaute_id):
    """ Afficher les posts d'une communaute """

    posts = Post.objects.filter(communaute__id=communaute_id)
    communaute_selectionnee = Communaute.objects.get(id=communaute_id)
    return render(request, 'communitymanager/communaute.html', locals())

def modifier_abonnement(request, communaute, user, modification):
    if modification :
        communaute.abonnes.add(user)
    else:
        communaute.abonnes.remove(user)
    return render(request, 'communitymanager/communautes.html', locals())
