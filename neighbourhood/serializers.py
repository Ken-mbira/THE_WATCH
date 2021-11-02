from rest_framework import serializers

from neighbourhood.models import Neighbourhood
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