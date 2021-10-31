from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
import neighbourhood

from neighbourhood.models import EventType, Neighbourhood,Location, Occurrence,Profile,Business,Services
from neighbourhood.serializers import NeighbourhoodSerializer,LocationSerializer, ProfileSerializer,BusinessSerializer, ServicesSerializer, EventsSerializer, OccurrenceSerializer



class NeighbourhoodList(generics.ListCreateAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer
    permission_classes = [IsAuthenticated]

class NeighbourhoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer
    permission_classes = [IsAuthenticated]

class LocationsList(generics.ListAPIView):
    queryset = Location.objects.filter(parent__isnull=True)
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.profile)

class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class=ServicesSerializer

class EventList(generics.ListCreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventsSerializer

class OccurrenceList(generics.ListCreateAPIView):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user.profile, neighbourhood=self.request.user.profile.neighbourhood)