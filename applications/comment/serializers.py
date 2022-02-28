from rest_framework import serializers, request

from .models import Comment
from rest_framework.serializers import ModelSerializer


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = {'id', 'author', 'comment', 'image'}

    def create(self, validated_data):
        requests = self.context.get('requests')
        validated_data['author_id'] = request.user.id
        comment = Comment.objects.create(**validated_data)
        return comment


