from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from neighbourhood.models import *

from neighbourhood.serializers import *

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def neighbour_view(request):
    data = {}

    if request.method == 'GET':
        neighbourhoods = Neighbourhood.objects.all()
        data = NeighbourhoodSerializer(neighbourhoods,many=True).data
        
        return Response(data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = NeighbourhoodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(request)
            data['success'] = "The neighbourhood was created successfully"
            return Response(data,status = status.HTTP_201_CREATED)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def business_view(request):
    data ={}

    if request.method == 'GET':
        businesses = Business.objects.all()
        data = BusinessSerializer(businesses,many=True).data

        return Response(data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BusinessSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(request)
            data['success'] = "The bussiness was created successfully"

            return Response(data,status = status.HTTP_201_CREATED)

        else:
            data = serializer.errors
            return Response(data,status = status.HTTP_400_BAD_REQUEST)
