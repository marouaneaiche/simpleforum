from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, Forum, Post, Reply
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from .services import ProfileService, ForumService

def index(request):
    return HttpResponse("Welcome to our forum!")

def profile_service(request):
    profile_id = 1
    return HttpResponse(ProfileService.get_profile(profile_id))

def forum_service(request):
    forum_id = 1
    return HttpResponse(ForumService.get_forum(forum_id))

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = serializers.ReplySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = serializers.ForumSerializer
    permission_classes = [permissions.IsAuthenticated]

