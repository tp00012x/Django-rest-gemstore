from rest_framework import viewsets
from products_rest.serializers import ProductSerializer
from products.models import Products

class ProductsViewsets(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer