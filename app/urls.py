from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'Post', views.PostViewSet)
router.register(r'Reply', views.ReplyViewSet)
router.register(r'Profile', views.ProfileViewSet)
router.register(r'Forum', views.ForumViewSet)
router.register(r'User', views.UserViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('ProfileService/', views.profile_service, name='profile_service'),
    path('ForumService/', views.forum_service, name='forum_service'),
    path('api/', include(router.urls))
    ]
