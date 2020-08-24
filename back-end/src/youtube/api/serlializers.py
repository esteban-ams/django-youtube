from rest_framework import serializers
from youtube.models import Video, Comment


class VideoSerlializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'owner']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta: 
        model = Comment
        fields = ['id', 'owner']