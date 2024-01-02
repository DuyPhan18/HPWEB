from django.shortcuts import render
from order.models import Order
from product.models import Products
from django.contrib.auth.models import User 
from django.db.models import Sum
from django.db import models
# Create your views here.
def indexStaff(request):
    total_revenue = Order.objects.aggregate(sum_total_bill=Sum('total_bill', output_field=models.IntegerField())).get('sum_total_bill', 0)
    count_order = Order.objects.count()
    count_product = Products.objects.count()
    count_customer = User.objects.filter(is_staff = False).count()
    context = {'total_revenue':total_revenue,'count_order':count_order, 'count_product':count_product, 'count_customer':count_customer}

    return render(request, 'staff/indexStaff.html', context)


    