from django.contrib import admin
from .models import Category, BlogPost, Tag, Setting
from blog.forms import BlogPostForm

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Setting)
