from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from tinymce.models import HTMLField
from django.utils.deconstruct import deconstructible
import os
from uuid import uuid4

@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path
        
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as a random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path
        return os.path.join(self.path, filename)
        
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, blank=True)
    
    def post_count(self):
        posts = BlogPost.objects.filter(category=self)
        return len(posts)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        if not self.slug:
            self.slug = self.name.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.name.replace(" ", "-").lower()
            self.slug = slug.replace(":", "")
        force_update = False
        
        # If the instance already has been saved, set forced_update to True
        if self.id:
            force_update = True
            
        # Force an UPDATE SQL Query if we're editing 
        super(Category, self).save(force_update=force_update)
    
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True, blank=True)
    
    def post_count(self):
        posts = BlogPost.objects.filter(tags__name=self.name)
        return len(posts)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        if not self.slug:
            self.slug = self.name.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.name.replace(" ", "-").lower()
            self.slug = slug.replace(":", "")
        force_update = False
        
        # If the instance already has been saved, set forced_update to True
        if self.id:
            force_update = True
            
        # Force an UPDATE SQL Query if we're editing 
        super(Tag, self).save(force_update=force_update)
        
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    publish = models.BooleanField(default=True)
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    image = models.ImageField(upload_to=PathAndRename('blog/'), blank=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date = models.DateField('date published', default=datetime.today)
    
    body = HTMLField()
    
    def get_tags(self):
        return self.tags.all()
    
    def __init__(self, *args, **kwargs):
        super(BlogPost, self).__init__(*args, **kwargs)
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = self.title.replace(" ", "-").lower()
            self.slug = slug.replace(":", "")
        force_update = False
        
        # If the instance already has been saved, set forced_update to True
        if self.id:
            force_update = True
            
        # Force an UPDATE SQL Query if we're editing 
        super(BlogPost, self).save(force_update=force_update)
    
    def __str__(self):
        return self.title

class Setting(SingletonModel):
    posts_per_page = models.SmallIntegerField(default=10)
    
    def __str__(self):
        return "Blog Settings"