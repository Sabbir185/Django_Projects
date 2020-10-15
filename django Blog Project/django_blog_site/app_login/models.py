from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User --> username , email , password , first_name , last_name

class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE , related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics')