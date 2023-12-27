from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .forms import CreateUserForm, UpdateUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def user_list(request):
    user_list = User.objects.all()
    filter_status = request.GET.get('is_staff', '')

    if filter_status.lower() == 'true':
        user_list = User.objects.filter(is_staff=True)
    elif filter_status.lower() == 'false' :
        user_list = User.objects.filter(is_staff=False)

    context = {'user_list':user_list, 'filter_status':filter_status}

    return render(request, "user/user_list.html", context)

def view_user(request, id):
    user = get_object_or_404(User, pk=id)

    return render(request, "user/update_user.html", {'user':user})
def create_user(request):
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                form.add_error('password1', "Passwords do not match")
                form.add_error('password2', "Passwords do not match")
            else:
                form.save()
                print("SUCCESS")
                return HttpResponseRedirect(reverse('user:user_list'))
    else:
        form=CreateUserForm()
    context = {'form':form}
    return render(request, 'user/user_list.html', context)
def update_user(request, id):
    user = get_object_or_404(User, pk=id)
    form = UpdateUserForm(request.POST or None, instance=user)
    if request.method == "POST":
      
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 and password2 and password1 != password2:
                form.error('password2', "Passwords do not match")
            else:
                form.save()
                print("SUCCESS")
                return HttpResponseRedirect(reverse('user:user', args=[id]))
    else:
        form = UpdateUserForm()
    context = {'user':user, 'form':form}
    return render(request, 'user/update_user.html', context)