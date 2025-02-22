from rest_framework import serializers
from django.utils import timezone

from post.models import Comment, Post 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'body', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','title','author','body','publish','status','created_at','updated_at',
                  'comments']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','body','publish','status']


    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        status = validated_data.get('status') 
        if status == 'PB':
            instance.publish = timezone.now()
         
        instance.save()
        return instance  
      

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post_id','user_id', 'body', 'created_at', 'updated_at']


