from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from youtube.models import Video, Comment
from youtube.api.serlializers import VideoSerlializer, CommentSerializer

@csrf_exempt
def video_list(request):
    
    if request.method == 'GET':
        video = Video.objects.all()
        serializer = VideoSerlializer(video, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerlializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)
        

def video_detail(request, pk):

    error_message = 'Oops!!  The object does not exist, try creating a new one!'

    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return HttpResponse(error_message, status=404)

    if request.method == 'GET':
        serializer = VideoSerlializer(video)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = VideoSerlializer(video, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)

    elif request.method == 'DELETE':
        video.delete()
        return HttpResponse(status=204)