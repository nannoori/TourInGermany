from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)

# Admin.property
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)
