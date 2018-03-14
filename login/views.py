from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'login/index.html')

#def login(request, username, password):
 #   user = db.get(username)
  #  if user.password == password:
   #     return redirect('login/')
