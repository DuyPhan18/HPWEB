from django.shortcuts import render, get_object_or_404
from .models import Products
from django.db.models import Q
# Create your views here.
def product_list(request):
    products = Products.objects.all()
    query = request.GET.get('search')

    if query:
        products = Products.filter(Q(product_name__icontains=query))
    context = {'products':products, 'query':query}
    return render(request, "product/product.html", context)
