from django.shortcuts import render
from .forms import VoucherForm
from .models import Voucher
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def voucher(request):
    vouchers = Voucher.objects.all()
    context = {'vouchers':vouchers}

    return render(request, 'voucher/voucher.html', context)

def create_voucher(request):
    form = VoucherForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():

            Voucher.create_voucher(form.cleaned_data)  
            return HttpResponseRedirect(reverse("voucher:voucher"))
    context = {'form':form}
    return render(request, "voucher/voucher.html", context)