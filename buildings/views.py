from django.shortcuts import render
from django.http import HttpResponse
from .models import Building, Floor, Room, Reservation
from django.http import Http404
from .forms import ReservationForm

# Create your views here.
def index(request):
    building_list = Building.objects.order_by('name')
    context = {'building_list' : building_list}
    return render(request, 'Website/Buildings.html', context)

def floors(request, building_name):
    try:
        building = Building.objects.get(name = building_name)
        floor_list = building.floor_set.order_by('name')
    except Building.DoesNotExist:
        raise Http404("Building does not exist")
    return render(request, 'Website/Floors.html', {'building': building, 'floor_list' : floor_list})

def rooms(request, building_name, floor_name):
    try:
        b = Building.objects.get(name = building_name)
        floor = Floor.objects.get(name = floor_name, building = b)
        room_list = floor.room_set.order_by('name')
    except Floor.DoesNotExist:
        raise Http404("Floor does not exist")
    return render(request, 'Website/Rooms.html', {'floor': floor, 'room_list' : room_list})

def displayRoom(request, building_name, floor_name, room):
    try:
        b = Building.objects.get(name = building_name)
        f = Floor.objects.get(name = floor_name, building = b)
        room = Room.objects.get(name = room, floor = f)
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if form.is_valid():
                dayReserved = form.cleaned_data.get('day')
                time = form.cleaned_data.get('timeInt')
                timeType = form.cleaned_data.get('timeType')
                if time > 0:
                    if form.timeWithTimeType(timeType=timeType, timeInt=time) != -1:
                        if timeType == 'pm':
                            if time != 12:
                                time += 12
                        if timeType == 'am':
                            if time == 12:
                                time += 12
                        if form.dayToInt(dayReserved) != -1:
                            if not room.calendar[form.dayToInt(dayReserved)][time]:
                                room.calendar[form.dayToInt(dayReserved)][time] = True
                                room.save()
                                r = Reservation(user = request.user, room = room, time = time, day=dayReserved)
                                r.save()
                                return HttpResponse('success')
        else:
            form = ReservationForm()
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'Website/displayRoom.html', {'room':room, 'form':form})
