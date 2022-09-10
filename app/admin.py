from django.contrib import admin

from .models import About, Contact, Career, Education, ProgrammingSkills, Skills, Feedbacks


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
    # save_as = True


    # fieldsets = (
    #     (None, {
    #         "fields": (("start", "end"),)
    #     }),
    # )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "role", "description")
    # fieldsets = (
    #     (None, {
    #         "fields": (("start", "end"),)
    #     }),
    # )


@admin.register(ProgrammingSkills)
class ProgrammingSkillsAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("title", "level")
    list_display_links = ('title',)


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("description",)
    
    # fieldsets = (
    #     ("MySkills", {
    #         "classes": ("collapse",),
    #         "fields": (("my_skills", "description"),)
    #     }),
    # )        


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    """Admin side of About section"""
    list_display = ("image", "name", "role", "description")


# admin.site.register(Skills)

