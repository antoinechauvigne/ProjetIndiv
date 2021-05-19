from django.urls import path
from . import views

urlpatterns = [
    path('', views.communautes, name='home'),
    path('communautes', views.communautes, name='communautes'),
    path('communautes/<int:communaute_id>/<int:modification>', views.communautes, name='modifier_abonnement'),
    path('communaute/<int:communaute_id>', views.communaute, name='communaute'),
    path('post/<int:post_id>', views.post, name='post'),

]
