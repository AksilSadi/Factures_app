from django.shortcuts import render
from django.http import HttpResponse
from .models import Produits, Factures, FacturesElements
from django.core.paginator import Paginator

# Create your views here.

def acceuil(request):
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

