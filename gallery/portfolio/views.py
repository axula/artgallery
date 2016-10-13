from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Category, Tag, GalleryPost, Setting

settings = Setting.objects.first()

def app_settings(request):
    return { 'css' : 'portfolio/style.css', 
             'app_settings' : Setting.objects.first() }
             
def paginate(request, post_list):
    paginator = Paginator(post_list, per_page=settings.thumbs_per_page, orphans=5)
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page
        return paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver last page of results
        return paginator.page(paginator.num_pages)

def index(request):
    gallery_posts = paginate(request, get_list_or_404(GalleryPost, publish=True))
    categories = Category.objects.all()
    return render(request, 'portfolio/index.html', RequestContext(request, { 'gallery_posts' : gallery_posts, 'categories' : categories }, [app_settings]))
    
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    gallery_posts = paginate(request, GalleryPost.objects.filter(category=category))
    categories = Category.objects.all()
    return render(request, 'portfolio/category.html', RequestContext(request, { 'category' : category, 'gallery_posts' : gallery_posts, 'categories' : categories }, [app_settings]))
    
def tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    gallery_posts = paginate(request, GalleryPost.objects.filter(tags__name=tag))
    categories = Category.objects.all()
    return render(request, 'portfolio/tag.html', RequestContext(request, { 'tag' : tag, 'gallery_posts' : gallery_posts, 'categories' : categories }, [app_settings]))
  
def gallerypost(request, category_slug, post_slug):
    post = get_object_or_404(GalleryPost, slug=post_slug, publish=True)
    images = post.images.all()
    tags = post.tags.all()
    
    previous = post.previous_post
    next = post.next_post
    return render(request, 'portfolio/gallerypost.html', RequestContext(request, { 'post' : post, 'images' : images, 'tags' : tags, 'next' : next, 'previous' : previous, }, [app_settings]))