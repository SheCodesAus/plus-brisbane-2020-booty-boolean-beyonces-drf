from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status, permissions
from django.http import Http404, HttpResponse, HttpResponseNotFound

# Create your views here.

class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
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
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

# 17.11: Trying to create a category view

class ProductCategory(APIView):

    def get(self, request, category): 
        # cateogry being passed in the request comes from the url
        products = Product.objects.all()
        products = products.filter(category__contains=category)
        # category__contains refers to the field "category" in the database        
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)
