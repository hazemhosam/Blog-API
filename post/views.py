from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from post.models import Comment, Post
from post.serializers import CommentCreateSerializer, CommentSerializer, PostSerializer, PostUpdateSerializer 


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
    
class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes =  [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id = self.kwargs['post_pk'])
    
    def create(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post_id=self.kwargs['post_pk'],user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class CommentDeatailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id = self.kwargs['post_pk'])


     


        

