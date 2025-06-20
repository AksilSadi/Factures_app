from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('factures/',views.factures, name='factures'),
    path('produits/', views.produits, name='produits'),
    path('produits/modifier/<int:id>/', views.modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:id>/', views.supprimer_produit, name='supprimer_produit'),
   
]