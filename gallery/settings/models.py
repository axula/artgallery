from __future__ import unicode_literals
from django.db import models

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
            
class Setting(SingletonModel):
    site_title = models.CharField(max_length=200)
    site_subtitle = models.CharField(max_length=200, blank=True)
    owner_name = models.CharField(max_length=200)
    owner_email = models.EmailField(blank=True)
    
    def __str__(self):
        return "Site Settings"
        
class NavigationMenu(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
        
class NavigationLink(models.Model):
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE, related_name="links")
    label = models.CharField(max_length=64)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)
    
    def __str__(self):
        return self.name