from django.urls import path 
from . import views
urlpatterns = [
    path('posts/',views.PostListCreateView.as_view()),
    path('posts/<int:pk>',views.PostDeatailView.as_view()),
    path('posts/<int:post_pk>/comments/',views.CommentListCreateView.as_view()),
    path('posts/<int:post_pk>/comments/<int:pk>',views.CommentDeatailView.as_view()),
]