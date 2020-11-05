from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'body', 'image', 'hashtag', 'hashtag2', 'hashtag3', 'hashtag4', 'hashtag5', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer): # new

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)