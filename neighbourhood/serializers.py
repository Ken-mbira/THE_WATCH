from rest_framework import serializers

from neighbourhood.models import Profile,Neighbourhood
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