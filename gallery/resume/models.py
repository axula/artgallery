from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.utils.deconstruct import deconstructible
from tinymce.models import HTMLField
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

class Resume(SingletonModel):
    full_name = models.CharField(max_length=64, unique=True)
    job_title = models.CharField(max_length=128, blank=True)
    # contact type
    
    image = models.ImageField(upload_to=PathAndRename('resume/'), blank=True)
    about = HTMLField()
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=64, blank=True)
    # social media
    
    specializations = HTMLField()
    skills = HTMLField()
    
    def __str__(self):
        return self.full_name + "'s resume"
    
class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name="experience")
    publish = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    start_date = models.DateField('start date', blank=True, null=True)
    end_date = models.DateField('end date', blank=True, null=True)
    description = HTMLField(blank=True)
    
    def __str__(self):
        return self.title
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name="education")
    publish = models.BooleanField(default=True)
    degree = models.CharField(max_length=128)
    school = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    date = models.DateField('date')
    description = HTMLField(blank=True)
    
    def __str__(self):
        return self.degree