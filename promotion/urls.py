from django.urls import path
from . import views

app_name = 'promotion'

urlpatterns = [
    path('', views.promote, name='promotion'),
    path('create_promote/', views.create_promote, name='create_promote')

]