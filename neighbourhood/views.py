from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from neighbourhood.models import Neighbourhood
from neighbourhood.serializers import NeighbourhoodSerializer


class NeighbourhoodList(generics.ListCreateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer
    permission_classes = [IsAuthenticated]