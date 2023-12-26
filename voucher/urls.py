from django.urls import path
from . import views

app_name = 'voucher'

urlpatterns = [
    path('', views.voucher, name='voucher'),
    path('creatte_voucher/', views.create_voucher, name="create_voucher")

]