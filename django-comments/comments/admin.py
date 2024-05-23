from django.contrib import admin

from comments.models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'user', 'content', 'creation_date', 'is_removed']
    search_fields = ['content']
    readonly_fields = ['content_type', 'object_id', 'user', 'creation_date', 'content', 'content_object']
