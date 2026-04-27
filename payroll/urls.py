from django.urls import path
from . import views

urlpatterns = [
    path('', views.payrollList, name='payrollList'),
    path('create/', views.payrollCreate, name='payrollCreate'),
    path('approve/<int:pk>/', views.payrollApprove, name='payrollApprove'),
    path('pay/<int:pk>/', views.payrollPay, name='payrollPay'),
]