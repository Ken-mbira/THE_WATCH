from django.db.models import fields
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from neighbourhood.models import EventType, Occurrence, Profile,Neighbourhood,Location,Profile,Business,Services
from account.models import Account
from account.serializers import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    """Defines the details to be included in serializing a profile

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Profile
        fields ='__all__'
        read_only_fields = ['account']

class NeighbourhoodSerializer(serializers.ModelSerializer):
    """Defines the details to be included in serializing a profile

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Neighbourhood
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    """This returns a list of locations

    Args:
        serializers ([type]): [description]
    """
    children = RecursiveField(many=True)
    class Meta:
        model = Location
        fields = ['id','name','children']


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ['owner']

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'

class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = '__all__'
        read_only_fields = ['reporter','neighbourhood']
