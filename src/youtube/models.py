from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(blank=False, null=False)
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(blank=False, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)