from django.conf.urls import url
from . import views

app_name = 'resume'

urlpatterns = [
    # /resume/
    url(r'^$', views.index, name='index')
]