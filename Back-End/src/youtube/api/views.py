from youtube.models import Video, Comment
from youtube.api.serlializers import VideoSerlializer, CommentSerializer
from rest_framework import generics

class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerlializer

class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerlializer







"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
class VideoList(APIView):

    def get(self, request, format=None):    
        video = Video.objects.all()
        serializer = VideoSerlializer(video, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = VideoSerlializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class VideoDetail(APIView):

    error_message = 'Oops!!  The object does not exist, try creating a new one!'

    def get_object(self, pk):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerlializer(video)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        video = self.get_object(pk)
        serializer = VideoSerlializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        video = self.get_object(pk)
        video.delete()
        return Response(status=status.HTTP_200_OK)
"""