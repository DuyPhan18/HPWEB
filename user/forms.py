from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    email = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput)
    is_staff = forms.BooleanField()

    class Meta:
        model = User  # Chỉ định lớp mô hình ở đây
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2', 'is_staff']
    
    def save(self):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user
class UpdateUserForm(forms.ModelForm):
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")    
        return password2
