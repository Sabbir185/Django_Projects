from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'app_post'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('like/<pk>/', views.like,name='like'),
    path('unlike/<pk>/',views.unlike,name='unlike'),
]