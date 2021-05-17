from django.urls import path
from . import views

urlpatterns = [
    path('', views.communautes, name='home'),
    path('communautes', views.communautes, name='communautes')

]
