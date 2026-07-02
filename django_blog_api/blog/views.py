from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by("-created_at")
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ["author"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "title"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
