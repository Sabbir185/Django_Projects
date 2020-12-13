from django.shortcuts import render

# import views
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# import models
from .models import Category,Product


# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'


class ProductDetails(DetailView,LoginRequiredMixin):
    model = Product
    template_name = 'app_shop/product_details.html'