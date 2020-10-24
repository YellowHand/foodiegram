from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    hashtag = models.CharField(max_length=50)
    hashtag2 = models.CharField(max_length=50)
    hashtag3 = models.CharField(max_length=50)
    hashtag4 = models.CharField(max_length=50)
    hashtag5 = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author