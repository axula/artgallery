from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Resume, Experience, Education

def app_settings(request):
    return { 'css' : 'resume/style.css' }
    
def index(request):
    resume = Resume.objects.first()
    experience = Experience.objects.filter(publish=True)
    education = Education.objects.filter(publish=True)
    
    return render(request, 'resume/index.html', RequestContext(request, { 'resume' : resume, 'experience' : experience, 'education' : education }, [app_settings]))
