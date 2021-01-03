from .models import Forum, Profile, Post, Reply
from django.contrib.auth.models import User
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'user', 'creation_date', 'last_edit_date', 'forum', 'title', 'content']


class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ['url', 'user', 'post', 'creation_date', 'last_edit_date', 'content']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'user', 'creation_date', 'user_level', 'location']
   

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ForumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forum
        fields = ['url', 'title']

