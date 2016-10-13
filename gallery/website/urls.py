from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^portfolio/', include('portfolio.urls')), 
    url(r'^blog/', include('blog.urls')), 
    url(r'^resume/', include('resume.urls')), 
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)