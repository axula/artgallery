from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Setting, NavigationMenu, NavigationLink
from settings.forms import NavMenuForm

class NavLinkInline(SortableInlineAdminMixin, admin.TabularInline):
    model = NavigationLink
    extra = 1
    
class NavMenuAdmin(admin.ModelAdmin):
    inlines = [ NavLinkInline, ]
    form = NavMenuForm

admin.site.register(Setting)
admin.site.register(NavigationMenu, NavMenuAdmin)