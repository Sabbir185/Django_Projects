from django.conf.urls import url
from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/' , views.sign_up, name='sign_up'),
    path('Login/', views.user_login, name='login_app'),
    path('Logout/', views.user_logout, name='user_logout'),
]
