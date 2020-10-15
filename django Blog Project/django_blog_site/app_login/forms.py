from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from app_login.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)