from django.urls import path
from . import views

urlpatterns = [
    path('', views.communautes, name='home'),
    path('communautes', views.communautes, name='communautes'),
    path('communautes/<int:communaute_id>/<int:modification>', views.communautes, name='modifier_abonnement'),
    path('communaute/<int:communaute_id>', views.communaute, name='communaute'),
    path('post/<int:post_id>', views.post, name='post'),
    path('nouveau_post', views.nouveau_post, name='nouveau_post'),
    path('modif_post/<int:post_id>', views.modif_post, name='modif_post'),
    path('posts', views.posts, name='posts'),

]
