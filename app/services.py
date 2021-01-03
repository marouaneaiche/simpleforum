from .models import Profile, Forum, Post, Reply
from django.contrib.auth.models import User

class ProfileService:

    @staticmethod
    def get_profile(profile_id):
        profile = Profile.objects.filter(id=profile_id)
        posts = Post.objects.filter(user=profile_id)
        replies = Reply.objects.filter(user=profile_id)
        
        #json representation of data
        json = '"service": "ProfileService"'
        return json


class ForumService:

    @staticmethod
    def get_forum(forum_id):
        forum = Forum.objects.filter(id=forum_id)
        posts = Post.objects.filter(forum=forum_id)
        
        #json representation of data
        json = '"service": "ForumService"'
        return json
