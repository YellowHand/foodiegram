from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('id', 'author', 'body', 'image', 'hashtag', 'hashtag2', 'hashtag3', 'hashtag4', 'hashtag5', 'created_at',)
        model = Post