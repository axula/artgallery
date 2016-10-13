from django import forms
from django.core.files.images import get_image_dimensions

from portfolio.models import GalleryPost

class GalleryPostForm(forms.ModelForm):
    class Meta: 
        model = GalleryPost
        exclude = []
        
    def clean_thumbnail(self):
        thumb = self.cleaned_data['thumbnail']
        if thumb:
            w, h = get_image_dimensions(thumb)
            
            if w < 300 or h < 300:
                raise forms.ValidationError("Please choose an image that is at least 300 x 300 pixels")
        return thumb