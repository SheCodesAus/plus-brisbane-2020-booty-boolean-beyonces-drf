from rest_framework import serializers
from .models import CustomUser
from products.serializers import ProductSerializer


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True) #data goes only one way into the database, calling it password makes it recognizable to create_user
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(max_length=80)
    location = serializers.CharField(required=False, allow_blank=True, max_length=80)
    fav = ProductSerializer(many=True)

    def __str__(self):
        return self.username