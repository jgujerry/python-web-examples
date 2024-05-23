from django.contrib import admin

from articles.models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at']
