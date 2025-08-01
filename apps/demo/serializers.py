# TODO There's certainly more than one way to do this task, so take your pick.

# apps/demo/serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # returns username

    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comment_count', 'comments']

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        # Latest 3 comments
        # To fetch 3 random comments instead of latest:
        # comments = obj.comments.order_by('?')[:3]
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data
