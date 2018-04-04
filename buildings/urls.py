from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:building_name>/', views.floors, name='floors'),
    path('<str:building_name>/<int:floor_name>/', views.rooms, name = 'rooms'),
    path('<str:building_name>/<int:floor_name>/<int:room>', views.displayRoom, name = 'displayRoom'),

]