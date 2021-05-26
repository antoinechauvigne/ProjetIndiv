from django.shortcuts import render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import CommentaireForm, NouveauPostForm
from .models import Communaute, Post, Commentaire


@login_required
def communautes(request, communaute_id=0, modification=2):
    """ Afficher les communautes et le statut d'abonnement
        C'est aussi la vue de la page d'accueil
    """

    # Nous sélectionnons toutes les instances de la classe Communaute
    list_communautes = get_list_or_404(Communaute)

    # Pour se désabonner
    if modification == 0:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.remove(request.user)
    # Pour s'abonner'
    elif modification == 1:
        communaute_modif = Communaute.objects.get(id=communaute_id)
        communaute_modif.abonnes.add(request.user)
    # Sinon il ne se passe rien

    # Obtention des données pour les envoyer au template
    for communaute in list_communautes:
        je_suis_abonne = False
        if request.user in communaute.abonnes.all():
            je_suis_abonne = True
        communaute.user_abonne = je_suis_abonne
        communaute.nb_posts = Post.objects.filter(communaute=communaute).count()

    return render(request, 'communitymanager/communautes.html', locals())


@login_required
def communaute(request, communaute_id):
    """ Afficher les posts d'une communaute """

    posts = Post.objects.filter(communaute__id=communaute_id).order_by('-date_creation')
    communaute_selectionnee = Communaute.objects.get(id=communaute_id)
    return render(request, 'communitymanager/communaute.html', locals())


@login_required
def post(request, post_id, suis_auteur=1):
    """ Afficher un post avec ses détails """

    mon_post = Post.objects.get(id=post_id)
    commentaires = Commentaire.objects.filter(post__id=post_id)
    sauvegarde = False
    form = CommentaireForm(request.POST or None)
    communaute_id = mon_post.communaute.id

    # Validation du formulaire de création de commentaire
    if form.is_valid():
        new_commentaire = form.save(commit=False)
        new_commentaire.auteur = request.user
        new_commentaire.post = mon_post
        new_commentaire.save()
        sauvegarde = True

    # En cas de non validation, retour à la même page
    return render(request, 'communitymanager/post.html', locals())


@login_required
def nouveau_post(request):
    """ Création un nouveau post """

    sauvegarde = False

    if request.method == "POST":
        form = NouveauPostForm(request.POST)
        # Une fois que le formulaire est validé, on peut afficher la page du post nouvellement créé
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auteur = request.user
            new_post.save()
            sauvegarde = True
            post_id = new_post.id
            return redirect('post', post_id)
    else:
        form = NouveauPostForm()
    # Permet le réappel de la même vue afin de valider le formulaire
    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required
def modif_post(request, post_id):
    """ Modification d'un post """

    sauvegarde = False
    post_modifie = Post.objects.get(id=post_id)
    suis_auteur = 0

    # If validé une fois que le formulaire a été soumis lors du réappel de la page
    if request.method == "POST":
        form = NouveauPostForm(request.POST or None, instance=post_modifie)
        if form.is_valid():
            sauvegarde = True
            form.save()
            return redirect('post', post_id)
        # En cas de formulaire invalide, vous renvoie vers la page pour rendre conforme votre modification
        else:
            return render(request, 'communitymanager/modifier_post.html', locals())
    else:
        # Permission de modification si et seulement si l'user connected est bien le créateur
        if post_modifie.auteur == request.user:
            form = NouveauPostForm(instance=post_modifie)
            return render(request, 'communitymanager/modifier_post.html', locals())
        # Sinon, renvoi vers la page du post avec un message de non autorisation
        else:
            return redirect('suis_auteur_post', post_id, suis_auteur)


@login_required
def posts(request):
    """ Afficher les posts appartenant aux commuautés d'abonnement """

    communautes_abonnes = Communaute.objects.filter(abonnes=request.user)
    list_posts = Post.objects.filter(communaute__in=communautes_abonnes).order_by('-date_creation')

    return render(request, 'communitymanager/posts.html', locals())
