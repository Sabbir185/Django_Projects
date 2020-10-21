from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class NewUserForm(UserCreationForm): 
     # if we add custom css design , crispy's some style will be gone
    email = forms.EmailField(required=True , label='' , widget=forms.TextInput(attrs={'placeholder':'Email'}))

    username = forms.CharField(required=True,label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))

    password1 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    password2 = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False,widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = UserProfile()
        exclude = ('user',)