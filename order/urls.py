from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.order_list, name="order_list"),
    path('create_order/', views.create_order, name="create_order")
]