from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse
from app_login.forms import SignUpForm,UserProfileForm

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method=='POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    return render(request,'app_login/sign_up.html',context={'form':form , 'registered':registered} )


def user_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

    return render(request,'app_login/sign_in.html',context={'form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login_app'))