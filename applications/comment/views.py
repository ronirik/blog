from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer
from Blog.applications.comment.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    comment = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]
