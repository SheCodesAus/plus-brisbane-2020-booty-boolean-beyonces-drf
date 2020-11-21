from rest_framework import serializers
from .models import CustomUser
from products.serializers import ProductSerializer
from products.models import Product
from django.http import Http404
from rest_framework import status

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True) #data goes only one way into the database, calling it password makes it recognizable to create_user
    first_name = serializers.CharField(max_length=80)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=80)
    location = serializers.CharField(required=False, allow_blank=True, max_length=80)
    image = serializers.URLField(max_length=200, required=False, allow_blank=True)
    add_fav = serializers.IntegerField(required=False, write_only=True)
    rem_fav = serializers.IntegerField(required=False, write_only=True)
    # I think by making add_fav and rem_fav write only fields then they wont be displayed, need to test
    fav = ProductSerializer(many=True, read_only=True)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) #changed to create_user rather than create to give us the ability to add the password the field
        #the password does not just get saved as data in the database, it seals it criptographically.


class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data): #instance will be the user in question
        instance.email = validated_data.get('email', instance.email) #only giving the user the ability to change their email
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.image = validated_data.get('image', instance.image)
        instance.location = validated_data.get('location', instance.location)


class CustomUserFavSerializer(CustomUserSerializer):

    def update(self, instance, validated_data): #instance will be the user in question
        add_fav = validated_data.get('add_fav', 0)
        rem_fav = validated_data.get('rem_fav', 0)

        # validated data will check if there is an add_fav and use it, otherwise it will use 0
        if add_fav is not 0:
            # check that the product exists
            try: 
                product=Product.objects.get(pk=add_fav) #gets the project with the relevant pk from the database
                # if it exists then add it to fav
                instance.fav.add(product)

            except Product.DoesNotExist:
                pass
               

        if rem_fav is not 0:
            # For later: How to check if that product is actually already in the list? Django would only remove if the item is in the list already, so no need to perform additional check
            try:
                product=Product.objects.get(pk=rem_fav)
                instance.fav.remove(product)

            except Product.DoesNotExist:
                pass 

        # add and remove save automatically, do not need instance.save in those occassions. 
        # However you do need to return the instace

        return instance