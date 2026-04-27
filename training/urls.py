from django.urls import path
from . import views

urlpatterns = [
    path('', views.sessionList, name='sessionList'),
    path('create/', views.sessionCreate, name='sessionCreate'),
    path('attendance/create/', views.attendanceCreate, name='attendanceCreate'),
]