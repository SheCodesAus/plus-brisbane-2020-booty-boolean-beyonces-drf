from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, CustomUserFavSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CustomUserList(APIView):
    def get(self,request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class CustomUserDetail(APIView):
    #So only after log in the user can change its details
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,  IsOwnerOrReadOnly] 

    # In previous project we were using isauthenticatedoreadonly, however in this one I am going to use authenticated only
    # 21/11: isauthenticated would let any user that is logged in change anything about any user, so we do need the is owner or read only
    def get_object(self,pk):
        try:
            user=CustomUser.objects.get(pk=pk) #gets the user with the relevant pk from the database
            self.check_object_permissions(self.request, user) #checks the permissions
            return user

        except CustomUser.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk): #put is used for putting some new info on a row on the database, as opposed to creating a whole new row
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True #this makes it ok if only some data is updated
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #this is not on the original pdf, added with Ollie
        
        return Response(serializer.errors) #it is good practice to always give a return when the data is not valid


class CustomUserFav(APIView):
    #So only after log in the user can change its details
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,  IsOwnerOrReadOnly] 
    def get_object(self,pk):
        try:
            user=CustomUser.objects.get(pk=pk) #gets the user with the relevant pk from the database
            self.check_object_permissions(self.request, user) #checks the permissions
            return user

        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserFavSerializer(user)
        # Returns Fav list only
        return Response(serializer.data)

    def put(self, request, pk): #put is used for putting some new info on a row on the database, as opposed to creating a whole new row
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserFavSerializer(
            instance=user,
            data=data,
            partial=True #this makes it ok if only some data is updated
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #this is not on the original pdf, added with Ollie
        
        return Response(serializer.errors) #it is good practice to always give a return when the data is not valid
                