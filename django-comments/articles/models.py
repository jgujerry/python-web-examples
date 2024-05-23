from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.db import models

from comments.models import Comment


# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)
    content = models.TextField(verbose_name='Content', blank=True, null=True)
    author = models.ForeignKey(User, related_name='articles', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Updated At', auto_now=True)
    
    # Add comment to this model
    comments = GenericRelation(Comment)
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Article'
        db_table = 'articles'
