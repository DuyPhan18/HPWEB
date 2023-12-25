from django.urls import path
from . import views
app_name = 'user'

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:id>/', views.view_user, name='user_info')

]