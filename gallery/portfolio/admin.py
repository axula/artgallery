from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Category, GalleryImage, GalleryPost, Tag, Setting
from portfolio.forms import GalleryPostForm

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    
class GalleryPostAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ GalleryImageInline, ]
    form = GalleryPostForm
    
    class Media:
        from django.conf import settings
        static = getattr(settings, 'STATIC_URL', '/static')
        js = ( static + 'js/admin.js', )

admin.site.register(Category)
admin.site.register(GalleryPost, GalleryPostAdmin)
admin.site.register(Tag)
admin.site.register(Setting)