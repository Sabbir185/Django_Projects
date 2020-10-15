from django.contrib import admin
from django.urls import path,include
from django_blog_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('app_blog.urls')),
    path('account/', include('app_login.urls')),
    path('', views.Index, name='index'),
]
