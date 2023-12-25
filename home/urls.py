from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/",views.login_handle, name= "login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path("register/",views.register, name="register"),
    path("user/<int:id>/", views.user_info, name="user"),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path("add_to_cart/<int:id>/", views.add_to_cart, name='add_to_cart'),
     path('update_cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('order_info/<int:id>/', views.view_order, name="order_info"),
    path('delete/<int:id>/', views.delete_from_cart, name='delete_from_cart')
]