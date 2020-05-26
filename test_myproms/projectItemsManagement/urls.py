from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accueil'),
    path ('quanti/<int:id>',views.lire, name='lire')
]
