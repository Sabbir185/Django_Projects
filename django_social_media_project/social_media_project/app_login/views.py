from django.shortcuts import render , HttpResponseRedirect , HttpResponse
from django.http import HttpResponse
from .forms import NewUserForm,ProfileForm
from .models import UserProfile,Follow
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from app_post.forms import PostForm
from django.contrib.auth.models import User

# Create your views here.

def sign_up(request):
    form = NewUserForm()
    registered = False
    if request.method == 'POST':
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'app_login/sign_up.html',context={'title':'Sign Up' , 'form':form })


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_post:home'))
    return render( request,'app_login/sign_in.html',context={'title':'Login' , 'form':form} )


@login_required
def edit_profile(request):
    current_user = request.user.user_profile
    form = ProfileForm(instance=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = ProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('app_login:user'))
    return render(request,'app_login/profile.html',context={'title':'Edit Profile','form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))

@login_required
def user_profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('app_login:user'))
    return render(request,'app_login/user.html',context={'title':'User Profile','form':form})


@login_required
def user_other(request,username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('app_login:user'))
    return render(request,'app_login/user_other.html',context={'user_other':user_other,'title':'View Other', 'already_followed':already_followed })


@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('app_login:user_other', kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('app_login:user_other', kwargs={'username':username}))
