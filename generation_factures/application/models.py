from django.db import models

# Create your models here.
class Produits(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom
    
class Factures(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.date_created.strftime('Facture du %d/%m/%Y')
    
    def get_montant(self):
     return sum(element.quantite * element.produit.prix for element in self.fac.all())
    
#table de jointure entre Factures et Produits
# pour stocker les quantités de chaque produit dans une facture
class FacturesElements(models.Model):
    facture = models.ForeignKey(Factures, related_name='fac', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} pcs"