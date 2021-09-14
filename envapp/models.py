from django.db import models

# Create your models here.

class Count(models.Model):
    idLocation = models.IntegerField()
    barcode = models.CharField(max_length=11)
    sku = models.CharField(max_length=17)
    urunAdi = models.CharField(max_length=40)
    locationCode = models.CharField(max_length=5)
    amount = models.IntegerField()

    def __str__(self):
        return self.urunAdi