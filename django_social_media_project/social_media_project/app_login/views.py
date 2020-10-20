from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse
from .forms import NewUserForm
# Create your views here.

def sign_up(request):
    form = NewUserForm()
    registered = False
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            pass
    return render(request,'app_login/sign_up.html',context={'title':'Sign Up' , 'form':form })