from django.conf.urls import url
from . import views

app_name = 'portfolio'
urlpatterns = [
    # /portfolio/
    url(r'^$', views.index, name="index"), 
    # /portfolio/category/category-slug/
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category, name="category"), 
    # /portfolio/tags/
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.tag, name="tag"), 
    # /portfolio/web/roadrunner_website
    url(r'^(?P<category_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.gallerypost, name="gallerypost")
]
