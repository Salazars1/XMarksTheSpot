from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('floors/', views.floors, name = 'floors'),
    path('rooms/', views.rooms, name = 'rooms'),
]