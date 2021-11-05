from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from account.serializers import RegistrationsSerializer
from .emails import send_welcome_email


@api_view(['POST',])
def register_view(request):
    data = {}
    
    serializer = RegistrationsSerializer(data = request.data)
    if serializer.is_valid():
        account = serializer.save()
        data['success'] = "The account was successfully created"
        return Response(data,status = status.HTTP_201_CREATED)

    else:
        data = serializer.errors
        return Response(data,status = status.HTTP_400_BAD_REQUEST)

