from rest_framework import serializers
from products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name','price','description','images','canPurchase')