from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'buildings/index.html')

def floors(request):
    return HttpResponse('This is the floors page.')

def rooms(request):
    return HttpResponse('This is the rooms page.')