from .models import Product_info
from rest_framework import serializers

class ProductSeri(serializers.ModelSerializer):
    class Meta:
        model = Product_info
        fields = '__all__'