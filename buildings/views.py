from django.shortcuts import render
from django.http import HttpResponse
from .models import Building, Floor, Room
from django.http import Http404

# Create your views here.
def index(request):
    building_list = Building.objects.all()
    context = {'building_list' : building_list}
    return render(request, 'Website/Buildings.html', context)

def floors(request, building_name):
    try:
        building = Building.objects.get(name = building_name)
    except Building.DoesNotExist:
        raise Http404("Building does not exist")
    return render(request, 'Website/Floors.html', {'building': building})

def rooms(request, building_name, floor_name):
    try:
        b = Building.objects.get(name = building_name)
        floor = Floor.objects.get(name = floor_name, building = b)
    except Floor.DoesNotExist:
        raise Http404("Floor does not exist")
    return render(request, 'Website/Rooms.html', {'floor': floor})