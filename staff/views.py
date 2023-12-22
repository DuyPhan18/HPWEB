from django.shortcuts import render

# Create your views here.
def indexStaff(request):
    return render(request, "staff/indexStaff.html")