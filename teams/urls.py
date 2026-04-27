from django.urls import path
from . import views

urlpatterns = [
    path('', views.teamList, name='teamList'),
    path('create/', views.teamCreate, name='teamCreate'),

    path('players/', views.playerList, name='playerList'),
    path('players/create/', views.playerCreate, name='playerCreate'),
]