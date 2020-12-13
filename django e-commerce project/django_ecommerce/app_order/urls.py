from django.conf import urls
from django.urls import path
from . import views

app_name = 'app_order'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name="add"),
]
