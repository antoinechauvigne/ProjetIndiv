from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import CommentaireForm, NouveauPostForm
from .models import Communaute, Post, Commentaire


# Create your views here.
@login_required
def communautes(request, communaute_id=0, modification=2):
    """ Afficher les communautes et le statut d'abonnement """

    # Nous sélectionnons toutes les instances de la classe Communaute
    list_communautes = get_list_or_404(Communaute)

    if modification == 0:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.remove(request.user)
    elif modification == 1:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.add(request.user)

    for communaute in list_communautes:
        je_suis_abonne = False
        if request.user in communaute.abonnes.all():
            je_suis_abonne = True
        communaute.user_abonne = je_suis_abonne

    return render(request, 'communitymanager/communautes.html', locals())

@login_required
def communaute(request, communaute_id):
    """ Afficher les posts d'une communaute """

    posts = Post.objects.filter(communaute__id=communaute_id)
    communaute_selectionnee = Communaute.objects.get(id=communaute_id)
    return render(request, 'communitymanager/communaute.html', locals())

@login_required
def post(request, post_id):
    """ Afficher un post """

    mon_post = Post.objects.get(id=post_id)
    commentaires = Commentaire.objects.filter(post__id=post_id)
    sauvegarde = False
    form = CommentaireForm(request.POST or None)

    if form.is_valid():
        new_commentaire = Commentaire()
        new_commentaire.date_creation = timezone.now()
        new_commentaire.contenu = form.cleaned_data["contenu"]
        new_commentaire.auteur = request.user
        new_commentaire.post = mon_post
        new_commentaire.save()
        sauvegarde = True

    return render(request, 'communitymanager/post.html', locals())

@login_required
def nouveau_post(request):
    """ Créer un nouveau post """

    sauvegarde = False
    form = NouveauPostForm(request.POST or None)
    print("je suis pret")
    if form.is_valid():
        print("je suis in")
        new_post = Post()
        new_post.titre = form.cleaned_data["titre"]
        new_post.description = form.cleaned_data["description"]
        new_post.date_creation = timezone.now()
        new_post.communaute = form.cleaned_data["communaute"]
        new_post.priorite = form.cleaned_data["priorite"]
        new_post.evenementiel = form.cleaned_data["evenementiel"]
        new_post.date_evenement = form.cleaned_data["date_evenement"]
        new_post.auteur = request.user
        new_post.save()
        sauvegarde = True
        print(new_post)
        #return render(request, 'communitymanager/post.html', locals())
    return render(request, 'communitymanager/nouveau_post.html', locals())