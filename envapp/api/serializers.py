
from rest_framework import serializers

from envapp.models import Count


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ["idLocation","barcode","sku","urunAdi","locationCode","amount"]

