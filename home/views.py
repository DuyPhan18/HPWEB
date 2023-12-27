from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from product.views import Products
from order.views import Order, OrderDetails
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder
from voucher.models import Voucher
from django.db.models import Q
# Create your views here.
def index(request):
    products = Products.objects.all()
    new_products = Products.objects.order_by("-date")[:5]
    best_products = Products.objects.order_by("-sold_quantity")[:5]


    for product in products:
            if product.promotion:
                product.product_price = product.product_price_on_sale
            else:
                product.product_price
    for product in new_products:
        if product.promotion:
            product.product_price = product.product_price_on_sale
        else:
            product.product_price

    for product in best_products:
        if product.promotion:
            product.product_price = product.product_price_on_sale
        else:
            product.product_price

    context={'products':products,'new_products': new_products,'best_products':best_products}
    return render(request, 'pages/index.html', context)

#All_product pages
def all_products(request):

    filter_cate = request.GET.get('cate', '')
    search_quuery = request.GET.get("search")
    if filter_cate.lower() == 'unisex':
        print("dđ:",filter_cate.lower() == 'unisex')
        products = Products.objects.filter(product_category__iexact='Unisex')
        print(products)
    elif filter_cate.lower() == 'bag':
        products = Products.objects.filter(product_category__iexact='bag')
    else:
        products = Products.objects.all()

    if search_quuery:
        products = Products.objects.filter(Q(product_name__icontains=search_quuery ))

    return render(request, 'pages/all_product.html', {'products':products,'filter_cate':filter_cate, 'search_quuery':search_quuery})
def user_info(request, id):
    user = get_object_or_404(User, pk=id)
    order = Order.objects.filter(user=id)
    return render(request, "pages/user_info.html", {'user':user, 'order':order})

def register(request): 
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {'form':form})
def product_detail(request, id):
    product_detail = get_object_or_404(Products, pk=id)
    return render(request, "pages/product_detail.html", {'product_detail':product_detail})
def login_handle(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
               
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')

    else:
        form = LoginForm()
    
    return render(request, 'pages/login.html', {'form':form})

def add_to_cart(request, id):
    product = get_object_or_404(Products, pk=id)
    cart = request.session.get('cart', {})
    # Thêm sản phẩm vào giỏ hàng hoặc cập nhật số lượng nếu đã tồn tại
    if product.promotion:
        product.product_price = product.product_price_on_sale

    cart[id] = {
        'product_name': product.product_name,
        'product_price': product.product_price,
        'quantity': cart.get(id, 0) + 1,
        'total_price': (cart.get(id, 0) + 1) * product.product_price,
    }
    cart_json = json.dumps(cart, cls=DjangoJSONEncoder)
    cart = json.loads(cart_json, parse_float=Decimal)

    # Lưu giỏ hàng mới vào session
    request.session['cart'] = cart
    request.session.modified = True

    return redirect("/")

def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        total_price = int(request.POST.get('total_price', 0))

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id]['quantity'] = quantity
            cart[product_id]['total_price'] = total_price
            request.session['cart'] = cart

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def view_cart(request):
    cart = request.session.get('cart',{})
    vouchers = Voucher.objects.all()
    # Tính toán total_quantity và total_bill
    total_quantity = sum(item.get('quantity', 0) for item in cart.values())
    total_bill = sum(int(item.get('total_price', 0)) for item in cart.values())

    context = {'cart': cart,'total_quantity': total_quantity, 'total_bill': total_bill, 'vouchers':vouchers}
    
    return render(request, 'pages/cart.html', context)
def view_order(request, id)  :
    order = get_object_or_404(Order, pk=id)
    order_info = OrderDetails.objects.filter(order=order)
    context = {'order':order, 'order_info':order_info}
    return render(request, 'pages/view_order.html', context)

def delete_from_cart(request, id):
    id = str(id)

    cart = request.session.get('cart',{})
   
    if id in cart:
        del cart[id]

    cart = request.session['cart'] 
    request.session.modified = True

    return render(request, 'pages/cart.html')