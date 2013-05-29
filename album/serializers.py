from django.forms import widgets
from rest_framework import serializers
from album.models import Picture, Comment

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image', 'title', 'description', 'pub_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'picture', 'author', 'description', 'pub_date')
