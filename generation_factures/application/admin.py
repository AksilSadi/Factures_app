from django.contrib import admin
from .models import Produits, Factures,FacturesElements
# Register your models here.
admin.site.register(Produits)
admin.site.register(Factures)
admin.site.register(FacturesElements)