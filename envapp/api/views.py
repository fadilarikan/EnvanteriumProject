from rest_framework.generics import ListAPIView

from envapp.api.serializers import ProductSerializer
from envapp.models import Count
from rest_framework import filters

class ProductListAPIView(ListAPIView):
    queryset = Count.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['locationCode']