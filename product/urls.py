from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('update_product/<int:id>/', views.update_product, name='update_product')
]