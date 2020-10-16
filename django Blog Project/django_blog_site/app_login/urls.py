from django.conf.urls import url
from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/' , views.sign_up, name='sign_up'),
    path('Login/', views.user_login, name='login_app'),
    path('Logout/', views.user_logout, name='user_logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('password/', views.update_password, name='password'),
    path('change-pic/', views.profile_pic_change, name='pic_change'),
    path('update-pic/', views.update_pic, name='update_pic'),
]
