from rest_framework import serializers
from .models import CustomUser


# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)
#     #New fields as of 13/09
#     password = serializers.CharField(write_only = True) #data goes only one way into the database, calling it password makes it recognizable to create_user
#     first_name = serializers.CharField(max_length=80)
#     last_name = serializers.CharField(max_length=80)