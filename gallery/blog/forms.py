from django import forms
from tinymce.widgets import TinyMCE

from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = []
        
    publish = forms.BooleanField(initial=False, required=False)