from django.urls import path
from . import views

urlpatterns = [
    path('', views.communautes, name='home'),
    path('communautes', views.communautes, name='communautes'),
    path('communaute/<communaute_id>', views.communaute, name='communaute')

]
