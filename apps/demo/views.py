# TODO There's certainly more than one way to do this task, so take your pick.

# apps/demo/views.py
from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'

class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    pagination_class = PostPagination
