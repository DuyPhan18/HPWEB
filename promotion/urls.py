from django.urls import path
from . import views

app_name = 'promotion'

urlpatterns = [
    path('', views.promote, name='promotion'),
    path('create_promote/', views.create_promote, name='create_promote'),
    path('<int:id>/', views.promote_detail, name='promote_detail'),
    path('update_promote/<int:id>/', views.update_promote, name='update_promote'),

]