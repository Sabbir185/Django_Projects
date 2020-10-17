from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>/' , views.blogDetails, name='blog_details'),
]