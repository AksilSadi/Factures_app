from django.shortcuts import render
from django.http import HttpResponse
from .models import Produits, Factures, FacturesElements
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def accueil(request):
    context = {
        'page_actuel': 'acceuil'
    }
    return render(request, 'acceuil.html',context)

def produits(request):
    # Récupère tous les produits
    liste_produits = Produits.objects.all().order_by('id')
    paginator = Paginator(liste_produits, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_actuel': 'produits'
    }

    return render(request, 'produits.html', context)

def factures(request):
    # Récupère toutes les factures
    liste_factures = Factures.objects.all().order_by('id')
    paginator = Paginator(liste_factures, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_actuel': 'factures'
    }

    return render(request, 'factures.html', context)

def modifier_produit(request, id):
    produit = get_object_or_404(Produits, id=id)

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prix = request.POST.get('prix')
        date_peremption = request.POST.get('date_peremption')

        # Met à jour le produit
        produit.nom = nom
        produit.prix = prix
        produit.date_peremption = date_peremption
        produit.save()

        return redirect('produits') 

    # si le get, on redirige ou on renvoie une erreur (optionnel)
    return redirect('produits')

def supprimer_produit(request, id):
    produit = get_object_or_404(Produits, id=id)

    if request.method == 'POST':
        # Supprime le produit
        produit.delete()
        return redirect('produits')

    # si le get, on redirige ou on renvoie une erreur (optionnel)
    return redirect('produits')
