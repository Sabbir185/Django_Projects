from django.urls import path
from . import views

app_name = "app_payment"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('pay/', views.payment, name="payment"),
    path('status/', views.complete, name="complete"),
    path('purchase/<val_id>/<tran_id>/', views.purchase, name="purchase"),
    path('order/', views.order_view, name="order"),
]
