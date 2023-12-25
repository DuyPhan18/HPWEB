from django.urls import path
from . import views

app_name = 'promote'

urlpatterns = [
    path('', views.promote, name='promote_home'),

]