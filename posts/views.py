from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


filter_backends = [
    DjangoFilterBackend,
    filters.OrderingFilter,
]


filterset_fields = ['category', 'author']

ordering_fields = ['published_at', 'title']

ordering = ['-published_at']
