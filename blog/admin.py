from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
    list_display = ['post', 'text', 'published_at', 'author',]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

