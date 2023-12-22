from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/",views.login_handle, name= "login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path("register/",views.register, name="register")
]