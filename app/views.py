from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ProfileView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(CreateAPIView):
    queryset = LikeSerializer


