from __future__ import unicode_literals
from datetime import datetime
from django.db import models
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
 
class GalleryPost(models.Model):
    publish = models.BooleanField(default=True)
    title = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, blank=True)
    thumbnail = models.ImageField(upload_to=PathAndRename('portfolio/thumbnails/'), blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    
    date = models.DateField('date published', default=datetime.today)
    credit = models.CharField(max_length=128, blank=True)
    medium = models.CharField(max_length=128, blank=True)
    client = models.CharField(max_length=128, blank=True)
    client_url = models.URLField(blank=True)
    project = models.CharField(max_length=128, blank=True)
    project_url = models.URLField(blank=True)
    
    description = models.TextField()
    
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)
        
    def previous_post(self):
        if self.order == 1:
            return GalleryPost.objects.order_by("-order")[0]
        else:
            return GalleryPost.objects.get(order=self.order-1)
    
    def next_post(self):
        last = GalleryPost.objects.order_by("-order")[0]
        if self.order == last.order:
            return GalleryPost.objects.get(order=1)
        else:
            return GalleryPost.objects.get(order=self.order+1)
    
    def create_thumbnail(self):
        # If the user has provided a thumbnail
        if self.thumbnail:
            return
            
        images = self.images.all()
        
        # If the post has no images
        if not images:
            return
            
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        image = images[0].get_image()
        
        if image.size[0] < image.size[1]:
            side = image.size[0]
        else:
            side = image.size[1]
        
        thumb = image.crop(( 0, 0, side, side ))
        
        DJANGO_TYPE = images[0].filetype()

        if DJANGO_TYPE == 'png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'
        else: # DJANGO_TYPE == 'jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
            
        # Save the thumbnail
        temp_handle = StringIO()
        thumb.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        
        suf = SimpleUploadedFile(os.path.split(images[0].image.url)[-1],
                temp_handle.read(), content_type=DJANGO_TYPE)
        
        self.thumbnail.save(
            '%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION),
            suf, save=False )
            
    def __init__(self, *args, **kwargs):
        super(GalleryPost, self).__init__(*args, **kwargs)
        self.create_thumbnail()
        if not self.slug:
            slug = self.title.replace(" ", "-").lower()
            self.slug = slug.replace(":", "")
    
    def save(self, *args, **kwargs):
        self.create_thumbnail()
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        force_update = False
        
        # If the instance already has been saved, set forced_update to True
        if self.id:
            force_update = True
            
        # Force an UPDATE SQL Query if we're editing 
        super(GalleryPost, self).save(force_update=force_update)
    
    def admin_thumb(self):
        return '<img src="%s"/>' % (self.thumbnail.url)
    admin_thumb.allow_tags = True
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    post = models.ForeignKey(GalleryPost, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=PathAndRename('portfolio/'))
    description = models.CharField(max_length=200, blank=True)
    alt_text = models.CharField(max_length=200, blank=True)
    
    def get_image(self):
        from PIL import Image
        from cStringIO import StringIO
        return Image.open(StringIO(self.image.read()))
        
    def filetype(self):
        return self.image.url.split('.')[-1].lower
        
class Setting(SingletonModel):
    thumbs_per_page = models.SmallIntegerField(default=20)
    
    def __str__(self):
        return "Portfolio Settings"