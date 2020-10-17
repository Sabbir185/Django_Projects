from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>/' , views.blogDetails, name='blog_details'),
    path('likes/<str:slug>/', views.like_post, name='like_post'),
    path('unlikes/<pk>/', views.unlike_post, name='unlike_post'),
    path('MyBlog/', views.MyBlog.as_view(), name='my_blog'),
    path('Edit-Blog/<pk>', views.EditBlog.as_view(), name='edit_blog'),
]