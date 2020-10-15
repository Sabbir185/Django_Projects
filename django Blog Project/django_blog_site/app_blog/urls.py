from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.home, name='blog_list'),
]