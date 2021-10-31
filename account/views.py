from django.shortcuts import render
from rest_framework import generics

from account.serializers import RegistrationsSerializer,UserSerializer
from account.models import Account

# Create your views here.

class UserList(generics.ListCreateAPIView):
    """Defines the endpoint for listing and creating a new user

    Args:
        generics ([type]): [description]
    """
    queryset = Account.objects.all()
    serializer_class = RegistrationsSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the endpoint for retrieving a specific user

    Args:
        generics ([type]): [description]
    """
    queryset = Account.objects.all()
    serializer_class = UserSerializer

