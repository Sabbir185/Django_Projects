from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    diction = {
        'fun':'ok'
    }
    return render(request,'app_blog/blog_list.html',context=diction)