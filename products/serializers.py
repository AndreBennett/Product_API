from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        title = Product
        fields = ['title', 'description', 'price', 'inventory_quantity']
        