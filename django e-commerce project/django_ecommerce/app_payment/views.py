from django.shortcuts import render , HttpResponseRedirect, redirect
from django.contrib import messages
from django.urls import reverse
# models and forms
from app_order.models import Order, Cart
from .models import BillingAddress
from .forms import BillingForm
from app_login.models import Profile

# for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f'Shipping Address saved !')

    # summery of order items
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    #print(order_qs)
    order_items = order_qs[0].orderItems.all()
    #print(order_items)
    order_total = order_qs[0].get_totals()

    return render(request,'app_payment/checkout.html', context={'form':form, 'order_items':order_items, 'order_total':order_total, 'saved_address':saved_address} )



@login_required
def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request,f"Please complete shipping address !")
        return redirect("app_payment:checkout")
    
    if not request.user.user_profile.is_fully_filled():
        messages.info(request,f'Please complete profile details !')
        return redirect('app_login:profile')

    # SSLcommerz api integration

    store_id = 'devhe5fde1ce99a0c1'
    api_key = 'devhe5fde1ce99a0c1@ssl'
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=api_key)


    status_url = request.build_absolute_uri(reverse('app_payment:complete'))
    #print(status_url)
    mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)


    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderItems.all()
    order_items_count = order_qs[0].orderItems.count()
    order_total = order_qs[0].get_totals()
    # above info
    mypayment.set_product_integration(total_amount=Decimal(order_total), currency='BDT', product_category='Mixed', product_name=order_items, num_of_item=order_items_count, shipping_method='Courier', product_profile='None')


    current_user = request.user
    # above info
    mypayment.set_customer_info(name=current_user.user_profile.full_name, email=current_user.email, address1=current_user.user_profile.address_1, address2=current_user.user_profile.address_1, city=current_user.user_profile.city, postcode=current_user.user_profile.zipcode, country=current_user.user_profile.country, phone=current_user.user_profile.phone)

    mypayment.set_shipping_info(shipping_to=current_user.user_profile.full_name, address=saved_address.address, city=saved_address.city, postcode=saved_address.zipcode, country=saved_address.country)

    response_data = mypayment.init_payment()
    #print(response_data)
    return redirect(response_data['GatewayPageURL'])



@csrf_exempt
def complete(request):
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST

        status = payment_data['status']

        if status=='VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            messages.success(request,f'Your payment completed successfully !')
            return HttpResponseRedirect(reverse('app_payment:purchase', kwargs={'val_id':val_id, 'tran_id':tran_id},))
        elif status=='FAILED':
            messages.info(request,f'Your payment failed! Please try again . Redirect home page after 10 seconds ')

    return render(request,'app_payment/complete.html', context={})


@login_required
def purchase(request, val_id, tran_id):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    orderId = tran_id
    order.ordered = True
    order.orderId = orderId
    Order.paymentId = val_id
    order.save()

    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()

    return HttpResponseRedirect(reverse('app_shop:home'))



@login_required
def order_view(request):
    try:
        orders = Order.objects.filter(user=request.user, ordered=True)
        diction = {'orders':orders}
    except:
        messages.warning(request,f"You don't have any active order")
    return render(request,'app_payment/order.html', context=diction)
