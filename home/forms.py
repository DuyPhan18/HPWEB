from django import forms
from django.contrib.auth.models import User
import re

class RegisterForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, required=True)
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput())
    password2 = forms.CharField(label="Re-Enter Password", widget = forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError("Error Password!")
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Username include special charater!")

        return username
        
    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'], 
            email=self.cleaned_data['email'], 
            password=self.cleaned_data['password2']
        )
class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

