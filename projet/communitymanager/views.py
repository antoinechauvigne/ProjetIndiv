from django.shortcuts import render, get_list_or_404, redirect
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
    communaute_id = mon_post.communaute.id

    if form.is_valid():
        new_commentaire = form.save(commit=False)
        new_commentaire.auteur = request.user
        new_commentaire.post = mon_post
        new_commentaire.save()
        sauvegarde = True

    return render(request, 'communitymanager/post.html', locals())

@login_required
def nouveau_post(request):
    """ Créer un nouveau post """

    sauvegarde = False
    print("je suis pret")
    if request.method == "POST":
        form = NouveauPostForm(request.POST) # or None)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auteur = request.user
            new_post.save()
            sauvegarde = True
            print(new_post)
            post_id=new_post.id

            return redirect('post', post_id)
            #return render(request, 'communitymanager/post.html', locals())
    else:
        form = NouveauPostForm()

    return render(request, 'communitymanager/nouveau_post.html', locals())


@login_required
def modif_post(request, post_id):
    """ Modifier un post """
    post_modifie = Post.objects.get(id=post_id)
    form = NouveauPostForm(request.POST or None, instance=post_modifie)

    if post_modifie.auteur==request.user:
        print("c'est ok, vous etes l'auteur du post")
        #print(form.cleaned_data)
        if form.is_valid():
            print("c'est ok, le formulaire est valide")
            form.save()

            #return redirect ('post', post_id)
        else:
            print("c'est PAS ok, le formulaire est INvalide")
    else:
        print ("vous n'etes PAS l'auteur du post")



    return render(request, 'communitymanager/modifier_post.html', locals())

def posts(request):
    """ Afficher les communautes et le statut d'abonnement """

    list_posts = get_list_or_404(Post)

    return render(request, 'communitymanager/posts.html', locals())

