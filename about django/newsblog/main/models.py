from django.db import models
from datetime import datetime

# Create your models here.
class story(models.Model):
    story_title = models.CharField(max_length=200)
    story_content = models.TextField(null=False, blank=True)
    story_published = models.DateTimeField("date published", default=datetime.now())
    story_image = models.ImageField(upload_to="image/", blank=True,null=True)

    def __str__(self):
        return self.story_title

class tech_news(models.Model):
    tech_news_title = models.CharField(max_length=200)
    tech_news_content = models.TextField(null=False, blank=True)
    tech_news_published = models.DateTimeField("date published", default=datetime.now())
    tech_news_image = models.ImageField(upload_to="image/", blank=True,null=True)

    def __str__(self):
        return self.tech_news_title
        