from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("tech/", views.tech_newspage, name="tech_newspage"),
]
