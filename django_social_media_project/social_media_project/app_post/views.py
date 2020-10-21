from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request,'app_post/home.html',context={'title':'Home'})
