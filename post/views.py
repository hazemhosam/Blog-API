from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from post.models import Post
from post.serializers import PostSerializer, PostUpdateSerializer 


class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.published.all() 

class PostDeatailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes =  [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.published.all() 
        
    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH']:
            return PostUpdateSerializer
        return PostSerializer 
        

