from django.contrib import admin
from .models import Item, Post, Comment

# Functional example first
admin.site.register(Item)
admin.site.register(Post)
admin.site.register(Comment)
# @admin.register(Post)
# class 
