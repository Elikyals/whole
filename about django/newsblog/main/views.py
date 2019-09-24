from django.shortcuts import render
from django.http import HttpResponse
from .models import story,tech_news
# from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"storys": story.objects.all})

def tech_newspage(request):
    return render(request=request,
                  template_name="main/tech_news.html",
                  context={"tech_newss": tech_news.objects.all})



# def register(request):
#     form = UserCreationForm
#     return render(request,
#                     "main")