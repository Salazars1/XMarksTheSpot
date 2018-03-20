from django.shortcuts import render
from django.http import HttpResponse
from .models import Building

# Create your views here.
def index(request):
    building_list = Building.objects.all()
    context = {'building_list' : building_list}
    return render(request, 'Website/Buildings.html', context)

def detail(request, building_id):
    return HttpResponse("You're looking at building %s." % building_id)

def floors(request):
    context = {}
    return render(request, 'Website/Floors.html')

def rooms(request):
    context = {}
    return render(request, 'Website/Rooms.html')