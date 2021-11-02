from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from neighbourhood.models import Neighbourhood

from neighbourhood.serializers import NeighbourhoodSerializer

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
