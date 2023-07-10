from django import forms
from django.contrib import admin

from .models import About, Contact, Career, Education, ProgrammingSkills, Skills, Testimonial, Works

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class WorksAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description = forms.CharField(label="Description", widget=CKEditorUploadingWidget())

    class Meta:
        model = Works
        fields = '__all__'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("my_name", "excerpt", "description")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("my_name", "address", "phone_number", "gmail")


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "role", "description")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "role", "description")


@admin.register(ProgrammingSkills)
class ProgrammingSkillsAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "level")
    list_display_links = ('title',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("description",)       


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "description", "image",)
    form = WorksAdminForm


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("name", "lastname", "job_title", "image", "description")