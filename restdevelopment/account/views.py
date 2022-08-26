from urllib import request
from .models import User
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class UserList(APIView):

    def get(self, request, format=None):
        userData = User.objects.all()
        serializer = UserSerializer(userData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserCreateView(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserUpdateView(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        userData = self.get_object(pk)
        serializer = UserSerializer(userData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDeleteView(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        userData = self.get_object(pk)
        userData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)