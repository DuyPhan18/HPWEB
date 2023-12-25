from django.shortcuts import render
from product.models import Products
# Create your views here.
def promote(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, "promote/promote.html", context)