# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import ISAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

#Model view set has both list and detail view
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (ISAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    
    
# Without view sets
# class PostList(generics.ListCreateAPIView):
#     permission_classes = (ISAuthorOrReadOnly,)
#     queryset =  Post.objects.all()
#     serializer_class = PostSerializer
    
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (ISAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer