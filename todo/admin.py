from django.contrib import admin
from .models import Item, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Item)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


admin.site.register(Comment)
# @admin.register(Post)
# class
