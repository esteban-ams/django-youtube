from rest_framework import serializers
from youtube.models import Video, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    video = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'video']