from django.contrib import admin
from .models import story,tech_news
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class storyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date/image ", {"fields": ["story_title", "story_published","story_image"]}),
        ("Content", {"fields": ["story_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }    

admin.site.register(story, storyAdmin)

class tech_newsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date/image ", {"fields": ["tech_news_title", "tech_news_published","tech_news_image"]}),
        ("Content", {"fields": ["tech_news_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    } 


admin.site.register(tech_news, tech_newsAdmin)