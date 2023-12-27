from django import forms
from .models import Promotes
class CreatePromoteForm(forms.ModelForm):
    class Meta:
        model = Promotes
        fields = ['promote_name', 'discount', 'start_date', 'end_date', 'status', 'products']

class UpdatePromoteForm(forms.ModelForm):
    class Meta:
        model = Promotes
        fields = ['promote_name', 'discount', 'start_date', 'end_date', 'status', 'products']
