from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from neighbourhood.models import Profile,Neighbourhood,Location
from account.models import Account

class ProfileSerializer(serializers.ModelSerializer):
    """Defines the details to be included in serializing a profile

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Profile
        fields = '__all__'

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

