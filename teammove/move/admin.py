from django.contrib import admin
from .models import Post, Comment, Likes, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Category)