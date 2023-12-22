from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.indexStaff, name="home_staff"),
    path("product/", include("product.urls")),
]