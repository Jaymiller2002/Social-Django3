from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['id', 'first_name', 'last_name']

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ['id', 'title', 'image', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at']  

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']  

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at']  

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['id', 'user', 'post']  

class RepostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repost
        fields = ['id', 'user', 'post']

