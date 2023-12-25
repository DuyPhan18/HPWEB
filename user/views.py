from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
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
    user_info = get_object_or_404(User, pk=id)

    return render(request, "user/update_user.html", {'user_info':user_info})