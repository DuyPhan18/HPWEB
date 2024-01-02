from django.shortcuts import render, redirect, get_object_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Order, OrderDetails
from product.models import Products
from decimal import Decimal
from django.contrib.auth.decorators import login_required
# Create your views here.
def order_list(request):
    order_list = Order.objects.all()
    context = {'order_list':order_list}
    return render(request, "order/order_list.html", context)

@login_required(login_url='login')
def create_order(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})
        quantity = request.POST.get('quantity_choose')
        total_price = request.POST.get('total_price')
        print(product_id, quantity, total_price)
        if product_id in cart:
            cart[product_id]['quantity'] = quantity
            cart[product_id]['total_price'] = total_price
            
            cart_json = json.dumps(cart, cls=DjangoJSONEncoder)
            cart = json.loads(cart_json, parse_float=Decimal)

        # Lưu giỏ hàng mới vào session
        request.session['cart'] = cart
        request.session.modified = True
        print(cart)
 
        user = request.user
        total_quantity = request.POST.get('total_quantity')
        total_bill = request.POST.get('total_bill')
        voucher = request.POST.get('voucher')
        if voucher:
           total_bill = int(total_bill) - (int(total_bill) * int(voucher) / 100)
        data = {
            'user': user,
            'total_quantity':total_quantity,
            'total_bill': total_bill
        }
        order = Order.objects.create(**data)
    
        #Lưu product item trong cart vào order details
        #dùng for lặp lấy key value trong cart
        cart = request.session.get('cart',{})
        for product_id, product_info in cart.items():
            try:
                print(product_info)
                product_name = product_info['product_name']
                product_price =  float(product_info['product_price'])
                quantity = product_info['quantity']
                total_price = product_info['total_price']
                print(product_price)

                # cập nhật lại quantity và sold_quantity
                product = get_object_or_404(Products, pk=product_id)
                product.product_quantity -= int(quantity)
                product.sold_quantity += int(quantity)
                product.save()

                detail_data = {
                    'order':order,
                    'product_name':product_name,
                    'product_price':product_price,
                    'quantity':quantity,
                    'total_price':total_price
                }
                
                # lưu vào order_detail
                order_detail = OrderDetails.create_order_detail(detail_data)
            except Exception as e:
                print(f"Error creating OrderDetails: {e}")
           #xóa cart khỏi session
        if 'cart' in request.session:
                del request.session['cart']
        return redirect("/")
    else:
        return render(request, "pages/cart.html")
    
def view_order(request, id):
    order = get_object_or_404(Order, pk = id)
    
    order_detail = OrderDetails.objects.filter(order=order)

    return render(request, "order/order_detail.html", {'order':order, 'order_detail':order_detail})
    