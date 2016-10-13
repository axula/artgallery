from django.contrib import admin
from .models import Resume, Experience, Education
from resume.forms import ResumeForm

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1
    
class ResumeAdmin(admin.ModelAdmin):
    inlines = [ ExperienceInline, EducationInline, ]
    form = ResumeForm

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Experience)
admin.site.register(Education)