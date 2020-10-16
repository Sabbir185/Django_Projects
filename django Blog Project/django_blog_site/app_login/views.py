from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse
from app_login.forms import SignUpForm,ProfilePicForm,UserProfileChange

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,PasswordChangeForm
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


@login_required
def user_profile(request):
    return render(request,'app_login/profile.html',context={})


@login_required
def update_profile(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    changed = False
    if request.method == "POST":
        form = UserProfileChange(instance=current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed = True

    return render(request,'app_login/update_profile.html',context={'form':form , 'changed':changed })


@login_required
def update_password(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    changed = False
    if request.method == "POST":
        form = PasswordChangeForm(current_user , data=request.POST)
        if form.is_valid():
            form.save()
            changed=True

    return render(request,'app_login/change_password.html',context={'form':form , 'changed':changed})


@login_required
def profile_pic_change(request):
    form = ProfilePicForm()
    changed = False
    if request.method =="POST":
        form = ProfilePicForm(request.POST , request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            changed = True
            return HttpResponseRedirect(reverse('app_login:user_profile'))

    return render(request,'app_login/change_profile_pic.html',context={'form':form , 'changed':changed, })


@login_required
def update_pic(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    changed = False
    if request.method == "POST":
        form = ProfilePicForm(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            changed = True
            #return HttpResponseRedirect(reverse('app_login:user_profile'))

    return render(request,'app_login/change_profile_pic.html',context={'form':form, 'changed':changed, })


