from django.db import models
from django.contrib.auth.models import User

# enum type for user types (regular, moderator, administrator)
from .userlevel import UserLevel


#Profile entity has a one-to-one relationship with django's predefined User entity
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_level = models.IntegerField(default=UserLevel.REGULAR)
    location = models.CharField(max_length=100)


class Forum(models.Model):
    title = models.CharField(max_length=50)


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)


class Reply(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    content = models.CharField(max_length=10000)
