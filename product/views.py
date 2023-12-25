from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Products
from django.db.models import Q
from .forms import AddProductForm, UpdateProductForm
import datetime
# Create your views here.
def product_list(request):
    products = Products.objects.all()
    query = request.GET.get('search')

    if query:
        products = Products.filter(Q(product_name__icontains=query))
    context = {'products':products, 'query':query}
    return render(request, "product/product.html", context)

def add_product(request):
    form = AddProductForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            Products.add_product(form.cleaned_data)
            return HttpResponseRedirect(reverse('product:product_list'))
    else:
        form = AddProductForm()

    context = {'form':form}

    return render(request, "product/add_product.html", context)
    
def product_detail(request, id):
    product_detail = Products.objects.get(pk=id)
    return render(request, 'product/update_product.html', {'product_detail': product_detail})

def update_product(request, id):
    update_product = get_object_or_404(Products, pk=id)
    if request.method == "POST":
        form = UpdateProductForm(request.POST, request.FILES, instance=update_product)
        print(form.is_valid())
        if form.is_valid():
            data=form.cleaned_data
            update_product.update_product(data)
        return HttpResponseRedirect(reverse('product:product_list'))
            
    else:
        form = UpdateProductForm()
    context = {'update_product': update_product, 'form': form}
    return render(request, "product/update_product.html", context)