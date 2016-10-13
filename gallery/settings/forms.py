from django import forms
from settings.models import NavigationMenu

class NavMenuForm(forms.ModelForm):
    class Meta: 
        model = NavigationMenu
        exclude = []