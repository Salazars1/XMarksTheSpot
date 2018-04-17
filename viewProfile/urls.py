from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('edit-account', views.editAccount, name = 'editAccount'),
    path('cancel-reservation/<int:id>', views.cancelReservation, name = 'cancelReservation'),
    path('check-in/<int:id>', views.checkIn, name = 'checkIn')
]