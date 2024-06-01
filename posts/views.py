# posts/views.py
from rest_framework import generics

from .models import Post
from .permissions import ISAuthorOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (ISAuthorOrReadOnly,)
    queryset =  Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ISAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer