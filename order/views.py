from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Order
# Create your views here.
def order_list(request):
    order_list = Order.objects.all()
    context = {'order_list':order_list}
    return render(request, "order/order_list.html", context)

def create_order(request):
    if request.method == "POST":
        user = request.user
        total_quantity = request.POST.get('total_quantity')
        total_bill = request.POST.get('total_bill')
        data = {
            'user': user,
            'total_quantity':total_quantity,
            'total_bill': total_bill
        }
        Order.create_order(data)
        #Lưu product item trong cart vào order details
        #dùng for lặp lấy key value trong cart
        cart = request.session.get('cart',{})
        for product_id, product_info in cart.items():
            product_name = product_info['product_name']
            product_price = product_info['product_price']
            quantity = product_info['quantity']
            total_price = product_info['total_price']


        return redirect("/")
    else:
        return render(request, "pages/cart.html")
      