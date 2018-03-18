from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    path('', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    path('create-account/', views.createAccount, name='createAccount'),
]