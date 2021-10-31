from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from neighbourhood.models import Neighbourhood,Location
from neighbourhood.serializers import NeighbourhoodSerializer,LocationSerializer


class NeighbourhoodList(generics.ListCreateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer
    permission_classes = [IsAuthenticated]

class LocationsList(generics.ListAPIView):
    queryset = Location.objects.filter(parent__isnull=True)
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]