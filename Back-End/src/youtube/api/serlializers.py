from rest_framework import serializers
from youtube.models import Video, Comment


class VideoSerlializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Video
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta: 
        model = Comment
        fields = '__all__'