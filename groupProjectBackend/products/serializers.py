from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    category = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=50)
    os = serializers.CharField(required=False, allow_blank=True, max_length=None)
    model_tech = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec1 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec2 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec3 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec4 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec5 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    spec6 = serializers.CharField(required=False, allow_blank=True, max_length=None)
    image = serializers.URLField()
    price = serializers.IntegerField()
    justification = serializers.CharField(required=False, allow_blank=True, max_length=None)
    supplier1 = serializers.URLField(required=False, allow_blank=True)
    supplier2 = serializers.URLField(required=False, allow_blank=True)
    overview = serializers.CharField(required=False, allow_blank=True, max_length=None)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)



