from django.urls import path 
from . import views
urlpatterns = [
    path('posts/',views.PostListCreateView.as_view()),
    path('posts/<int:pk>',views.PostDeatailView.as_view())
]