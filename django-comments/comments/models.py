from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField


class Comment(models.Model):
    content = HTMLField(verbose_name='Content', max_length=512)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(verbose_name='Date/Time Created', default=timezone.now)
    is_removed = models.BooleanField(verbose_name='Is Removed', default=False)
    
    # Content-object fields
    content_type = models.ForeignKey(ContentType, verbose_name='Content-Type', on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField(verbose_name="Object ID", db_index=True)
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('createion_date')
