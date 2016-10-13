from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', views.index, name='index'),
    # /blog/category/category-slug/
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category, name="category"), 
    # /blog/tag/tag-slug/
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.tag, name="tag"), 
    # /blog/post-title
    url(r'^(?P<post_slug>[:\-\w]+)/$', views.blogpost, name="blogpost")
]