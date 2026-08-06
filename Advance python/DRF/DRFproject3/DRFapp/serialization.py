from .models import LaptopInfo
from rest_framework import serializers

class LaptopInfoSeri(serializers.ModelSerializer):
    class Meta:
        model = LaptopInfo
        fields = '__all__'