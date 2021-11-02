from rest_framework import serializers

from neighbourhood.models import *
from account.serializers import UserSerializer

class NeighbourhoodSerializer(serializers.ModelSerializer):
    """This deals with parsing the neighbourhood model

    Args:
        serializers ([type]): [description]
    """
    admin = UserSerializer()

    class Meta:
        model = Neighbourhood
        fields = '__all__'
        read_only_fields = ['admin']

    def save(self,request):
        neighbourhood = Neighbourhood(name = self.validated_data['name'],location = self.validated_data['location'],slogan = self.validated_data['slogan'],police_hotline = self.validated_data['police_hotline'],hospital_hotline = self.validated_data['hospital_hotline'],image = self.validated_data['image'],admin = request.user)
        neighbourhood.save()


class ServiceSerializer(serializers.ModelSerializer):
    """Deals with parsing services into the requests

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Services
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    """This interchanges data pertaining the business class

    Args:
        serializers ([type]): [description]
    """
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Business
        fields = '__all__'

    def save(self,request):
        business = Business(owner = request.user,name = self.validated_data['name'],services = self.validated_data['services'],image = self.validated_data['image'])

        business.save()

class OccurrenceSerializer(serializers.ModelSerializer):
    """This deals with parsing the occurences

    Args:
        serializers ([type]): [description]
    """
    reporter = UserSerializer(read_only=True)
    class Meta:
        model = Occurrence
        fields = '__all__'
        read_only_fields = ['neighbourhood']

    def save(self,request,neighbourhood):
        occurence = Occurrence(type = self.validated_data['type'],neighbourhood = neighbourhood,reporter = request.user, name = self.validated_data['name'],description = self.validated_data['description'],image_description = self.validated_data['image_description'],to_happen_at = self.validated_data['to_happen_at'])
        occurence.save()