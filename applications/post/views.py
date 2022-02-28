from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .permissions import IsQuestionAuthor
from .serializers import PostSerializer




# Question crate view
class PostListView(generics.ListAPIView):
    post = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]

    def get_serializer_context(self):
        return {'request': self.request}


class PostUpdateView(generics.UpdateAPIView):
    post = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsQuestionAuthor]

class PostDeleteView(generics.DestroyAPIView):
    post = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor]
