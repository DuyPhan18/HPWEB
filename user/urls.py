from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.view_user, name='user'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),

]