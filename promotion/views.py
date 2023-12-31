from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from product.models import Products
from .forms import CreatePromoteForm, UpdatePromoteForm
from .models import Promotes
from decimal import Decimal
from django.urls import reverse
from django.utils import timezone
# Create your views here.
def promote(request):

    products = Products.objects.all()
    promote_list = Promotes.objects.all()

    context = {'products': products, 'promote_list':promote_list}
    return render(request, "promotion/promote.html", context)
    

def create_promote(request):
    form = CreatePromoteForm(request.POST, request.FILES)
    print(form.is_valid())
    print(form.errors)
    print(request.POST.get("discount"))
    if form.is_valid():
        # Lấy dữ liệu đã được làm sạch từ form
        cleaned_data = form.cleaned_data
        discount = Decimal(request.POST.get("discount", 0))
        products_id_list = cleaned_data.pop('products', [])
        
        product_list = Products.objects.filter(pk__in=products_id_list)

        for product in product_list:
            product_price = Decimal(product.product_price)
            product.product_price_on_sale = product_price - (product_price * discount / 100)
            product.promotion = "True"
            product.save()

            print('org:',product.product_price)
            print('new:',product.product_price_on_sale)


        Promotes.objects.create(**cleaned_data)
        print('create success')
        return HttpResponseRedirect(reverse('promotion:promotion'))

    context ={'form':form}

    return render(request, "promotion/promote.html", context)

def promote_detail(request, id):
    promote_detail = Promotes.objects.get(pk=id)
    products = Products.objects.all()
    return render(request, 'promotion/update_promote.html', {'promote_detail': promote_detail, 'products': products})

def update_promote(request, id):
    update_promote = get_object_or_404(Promotes, pk=id)
    if request.method == "POST":
        form = UpdatePromoteForm(request.POST, instance=update_promote)
        if form.is_valid():
            data = form.cleaned_data
            update_promote.update_promote(data)
            return HttpResponseRedirect(reverse('promotion:promotion'))
    else:
        form = UpdatePromoteForm()
    context = {'update_promote': update_promote, 'form': form}

    return render(request, "promotion/update_promote.html", context)
