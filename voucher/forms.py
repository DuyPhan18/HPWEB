from django import forms
from .models import Voucher

class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['voucher_name', 'v_quantity', 'v_discount','status']