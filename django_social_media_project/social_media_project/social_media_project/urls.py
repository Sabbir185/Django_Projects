from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from app_post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('app_login.urls')),
    path('post/', include('app_post.urls')),
    path('', views.home, name='home')
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
