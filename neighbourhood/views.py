from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from neighbourhood.models import *
from account.serializers import *
from neighbourhood.serializers import *

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def neighbour_view(request):
    data = {}

    if request.method == 'GET':
        neighbourhoods = Neighbourhood.objects.all()
        data = GetNeighbourhoodSerializer(neighbourhoods,many=True).data
        
        return Response(data,status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = NeighbourhoodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(request)
            data['success'] = "The neighbourhood was created successfully"
            return Response(data,status = status.HTTP_201_CREATED)

        else:
            data = serializer.errors
            return Response(data,status = status.HTTP_400_BAD_REQUEST)

class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_neighbourhood(request,pk):
    data = {}
    profile = Profile.objects.get(user = request.user)
    neighbourhood = Neighbourhood.objects.get(pk=pk)
    profile.neighbourhood = neighbourhood
    profile.save()
    data['success'] = f"You successfully joined ${neighbourhood.slogan}"
    return Response(data,status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def move_out(request):
    data = {}
    profile = Profile.objects.get(user = request.user)
    profile.neighbourhood = None
    profile.save()
    data['success'] = "You are no longer a member of the neighbourhood!"
    return Response(data,status = status.HTTP_200_OK)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_neighbourhood(request):
    data = {}
    profile = Profile.objects.get(user = request.user)
    print(profile.neighbourhood)
    data = ProfileSerializer(profile).data
    return Response(data,status = status.HTTP_200_OK)

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

@api_view(['POST','GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def occurence_view(request,pk):
    data = {}

    try:
        neighbourhood = Neighbourhood.objects.get(pk=pk)
    except :
        data['not found'] = "The neighbourhood was not found"
        return Response(data,status = status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = OccurrenceSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(request,neighbourhood)
            data['success'] = "The occurrence was successfully reported"
            return Response(data,status = status.HTTP_200_OK)

        else:
            data = serializer.errors
            print(data)
            return Response(data,status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        events = Occurrence.get_events(pk)
        data = OccurrenceSerializer(events,many=True).data

        return Response(data,status= status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_businesses(request,pk):
    """The view for getting all businesses in a neighbourhood

    Args:
        request ([type]): [description]
        pk ([type]): [description]
    """
    businesses = Business.get_bussinesses(pk)
    data = {}
    data['businesses'] = BusinessSerializer(businesses,many=True).data

    return Response(data,status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_residents(request,pk):
    """This parses the request to get the users in a certain neighbourhood

    Args:
        request ([type]): [description]
        pk ([type]): [description]
    """
    data = {}
    users = Profile.get_residents(pk)

    data['users'] = UserSerializer(users,many=True).data
    return Response(data,status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_business(request,term):
    """This parses the view request for getting the businesses via a search term

    Args:
        request ([type]): [description]
    """
    data = {}

    results = Business.search_by_name(term)

    data['businesses'] = BusinessSerializer(results,many=True).data
    return Response(data,status=status.HTTP_200_OK)

class EventTypeList(generics.ListAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventSerializer
    permission_classes=[IsAuthenticated]