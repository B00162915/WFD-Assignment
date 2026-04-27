from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeList, name='employeeList'),
    path('create/', views.employeeCreate, name='employeeCreate'),
]