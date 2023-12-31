from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.indexStaff, name="home_staff"),
    path("product/", include("product.urls", namespace="product")),
    path("order/", include("order.urls", namespace="order")),
    path("user/", include("user.urls", namespace="user")),
    path("promotion/", include("promotion.urls", namespace="promotion")),
    path("voucher/", include("voucher.urls", namespace="voucher"))
]
