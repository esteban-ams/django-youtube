from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null= False)
    # file = models.FileField(upload_to='videos/uploads/')
    owner = models.ForeignKey('auth.User', related_name='video', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=True, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE)
       
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)