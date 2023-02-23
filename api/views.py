from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import SongSerializer
from .models import Song
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    
    routes=[
        {'GET':'/api/songs'},  
    ]
    return Response(routes)



@api_view(['GET'])
def get_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_song(request, pk):
    try:
        song = Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SongSerializer(song, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_song(request, pk):
    try:
        song = Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(song, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_song(request, pk):
    try:
        song = Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)