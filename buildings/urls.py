from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:building_id>/', views.detail, name='detail'),
    path('floors/', views.floors, name = 'floors'),
    path('rooms/', views.rooms, name = 'rooms'),
]