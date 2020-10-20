from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/' , views.sign_up , name='sign_up' )
]
