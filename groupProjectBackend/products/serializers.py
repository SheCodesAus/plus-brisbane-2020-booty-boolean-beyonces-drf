from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    category = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=50)
    spec1 = serializers.CharField(max_length=None)
    spec2 = serializers.CharField(max_length=None)
    spec3 = serializers.CharField(max_length=None)
    spec4 = serializers.CharField(max_length=None)
    spec5 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    image = serializers.URLField()
    price = serializers.IntegerField()
    supplier1 = serializers.URLField()
    supplier2 = serializers.URLField()


    def create(self, validated_data):
        return Product.objects.create(**validated_data)