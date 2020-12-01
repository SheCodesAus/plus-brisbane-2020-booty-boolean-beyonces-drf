from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status, permissions
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.db.models import Exists, OuterRef
# from rest_framework.exceptions import APIException
# from rest_framework.permissions import IsAuthenticated



# Create your views here.

class ProductList(APIView):

    def get(self, request):

        if request.user.is_anonymous:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        
        else:
    
            # The beloew is_fav works when the user is logged in, but if there is not user
            # it fails to load any products - need to keep working on it
             # 29/11: annotate sets is_fav to True if the product has been favourited by the user in the request
            # is_fav: can then be used to put a little star to indicate it has been favourited already
            user_fav = request.user.fav.filter(id = OuterRef('pk'))
            products = Product.objects.all().annotate(is_fav = Exists(user_fav))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        
        
    def post(self, request): 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() #this will assign the logged in user as the project owner
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProductDetail(APIView):
   
    def get_object(self, pk):
        try:
            product=Product.objects.get(pk=pk) #gets the project with the relevant pk from the database
            # self.check_object_permissions(self.request, project)
            return product

        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):

        # This checks if user is anonymous then it gives back all that is in the database
        if  request.user.is_anonymous:
            product = self.get_object(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

         # AA 01.12 - if the user is not anonymous, e.g. logged in, then it annotates is_fav
        else:
            is_fav = request.user.fav.filter(pk=pk).exists()
            product = self.get_object(pk)
            product.is_fav = is_fav
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 17.11: Trying to create a category view

class ProductCategory(APIView):

    def get(self, request, category): 

        # This checks if user is anonymous then it gives back all that is in the database

        if request.user.is_anonymous:
            products = Product.objects.all()
            products = products.filter(category__contains=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        # AA 01.12 - if the user is not anonymous, e.g. logged in, then it annotates is_fav
        else: 
            user_fav = request.user.fav.filter(id = OuterRef('pk'))
            products = Product.objects.all().filter(category__contains=category).annotate(is_fav = Exists(user_fav))
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        

        
