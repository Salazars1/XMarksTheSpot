from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'registration/login.html')

def createAccount(request):
    return render(request, 'Website/CreateAccount.html')

