from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from product.views import Products
from order.views import Order
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
def index(request):
    products = Products.objects.all()

    context={'products': products}
    return render(request, 'pages/index.html', context)

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
                messages.success(request, 'Login success')
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

def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def view_cart(request):
    cart = request.session.get('cart',{})
    # Tính toán total_quantity và total_bill
    total_quantity = sum(item.get('quantity', 0) for item in cart.values())
    total_bill = sum(int(item.get('total_price', 0)) for item in cart.values())
    return render(request, 'pages/cart.html', {'cart': cart,'total_quantity': total_quantity, 'total_bill': total_bill})
    
def delete_from_cart(request, id):
    id = str(id)

    cart = request.session.get('cart',{})
   
    if id in cart:
        del cart[id]

    cart = request.session['cart'] 
    request.session.modified = True

    return render(request, 'pages/cart.html')