from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from rest_framework import status
from rest_framework.response import Response
import requests
import jwt
import os

class Views:

    def verify_authentication(self, request, callback):
        access_token : str = request.headers['Authorization'] 
        access_token = access_token.split(' ')[1]
        
        #print(access_token)
        body = {"token" : access_token}
        #print(body)
        validacao = requests.post(url=f'{os.getenv('AUTH_URL')}api/token/verify/', data=body)
        validacao = validacao.json()
        #print(f"validando:{validacao}")

        if validacao != {}:
            return Response(validacao, status=status.HTTP_401_UNAUTHORIZED)
        
        return callback(request)


class CreateUserView(generics.CreateAPIView, Views):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        #print('oi')
        return self.verify_authentication(request, self.create)


class GetAllView(generics.ListAPIView, Views):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.verify_authentication(request, self.list)

class GetUserView(generics.RetrieveAPIView, Views):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.verify_authentication(request, self.retrieve)



class PatchUserView(generics.UpdateAPIView, Views):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):
        return self.verify_authentication(request, self.partial_update)

    
