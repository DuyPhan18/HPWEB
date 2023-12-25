from django import forms
from .models import Products
import datetime
class AddProductForm(forms.ModelForm):
   class Meta:
        model = Products
        fields = ['product_name', 'product_price', 'product_image', 'product_desc', 'product_quantity', 'product_category', 'status']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_price', 'product_image', 'product_desc', 'product_quantity', 'product_category', 'status']