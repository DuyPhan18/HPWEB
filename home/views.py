from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def register(request): 
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'pages/register.html', {'form':form})

def login_handle(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    
    return render(request, 'pages/login.html', {'form':form})
