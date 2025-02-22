from django.utils import timezone
from django.conf import settings
from django.db import models

# An custom manger to filter the published posts 
class PublishedManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED) 
    

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR','Draft'
        PUBLISHED = 'PB','Published' 
        
    
    title = models.CharField(max_length=255)
    body= models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                               related_name='posts')
    publish = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,
                                           default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManger()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title 
    
