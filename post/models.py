from datetime import timezone
from django.conf import settings
from django.db import models

# An custom manger to filter the published posts 
class PublishedManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED) 
    

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR','Draft'
        published = 'PH','Published' 
        
    
    title = models.CharField(max_length=255)
    body= models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                               related_name='posts')
    published = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,
                                           defualt=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManger()

    class Meta:
        orderin = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]

    def __str__(self):
        return self.title 
    
