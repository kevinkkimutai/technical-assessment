from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ["id", "author", "title", "content", "created_at"]
        read_only_fields = ["id", "author", "created_at"]
