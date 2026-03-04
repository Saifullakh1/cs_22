from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ["id", "title", "description", "image", "created_at", "post_comments"]
