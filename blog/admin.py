from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']
    list_display = ['title', 'author', 'published_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']
    list_display = ['author', 'post', 'text']


admin.site.register(Tag)