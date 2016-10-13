from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Tag, BlogPost, Setting

settings = Setting.objects.first()

def app_settings(request):
    return { 'css' : 'blog/style.css', 
             'app_settings' : Setting.objects.first() }
             
def paginate(paginator, page):
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page
        return paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver last page of results
        return paginator.page(paginator.num_pages)

def index(request):
    post_list = get_list_or_404(BlogPost, publish=True)
    paginator = Paginator(post_list, per_page=settings.posts_per_page, orphans=1)
    page = request.GET.get('page')
    posts = paginate(paginator, page)
    return render(request, 'blog/index.html', RequestContext(request, { 'posts' : posts }, [app_settings]))
    
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    
    post_list = BlogPost.objects.filter(category=category, publish=True)
    paginator = Paginator(post_list, per_page=settings.posts_per_page, orphans=1)
    page = request.GET.get('page')
    posts = paginate(paginator, page)
    return render(request, 'blog/category.html', RequestContext(request, { 'css' : 'blog/style.css', 'category' : category, 'categories' : categories, 'posts' : posts }, [app_settings]))
    
def tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    tags = Tag.objects.all()
    
    post_list = BlogPost.objects.filter(tags__name=tag, publish=True)
    paginator = Paginator(post_list, per_page=settings.posts_per_page, orphans=1)
    page = request.GET.get('page')
    posts = paginate(paginator, page)
    return render(request, 'blog/tag.html', RequestContext(request, { 'css' : 'blog/style.css', 'tag' : tag, 'tags' : tags, 'posts' : posts }, [app_settings]))
    
def blogpost(request, post_slug):
    post_list = get_object_or_404(BlogPost, slug=post_slug, publish=True)
    paginator = Paginator(post_list, per_page=settings.posts_per_page, orphans=1)
    page = request.GET.get('page')
    posts = paginate(paginator, page)
    return render(request, 'blog/blogpost.html', RequestContext(request, { 'css' : 'blog/style.css', 'post' : post }, [app_settings]))