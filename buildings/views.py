from django.shortcuts import render
from django.http import HttpResponse
from .models import Building, Floor, Room, Reservation
from django.http import Http404
from .forms import ReservationForm
from django.shortcuts import redirect

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
    response = ''
    if not request.user.username:
        return redirect('login')
    try:
        b = Building.objects.get(name = building_name)
        f = Floor.objects.get(name = floor_name, building = b)
        room = Room.objects.get(name = room, floor = f)
        reservation_list = room.reservation_set.all()
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
                            reservation_list = Reservation.objects.filter(day = dayReserved, room = room)
                            available = True
                            for reservation in reservation_list:
                                if reservation.time == time:
                                    available = False
                            if available:
                                r = Reservation(user = request.user, room = room, time = time, day=dayReserved)
                                r.save()
                                room.save()
                                form = ReservationForm()
                                response = 'Room successfully reserved.'
                            else:
                                response = 'Room already reserved at that time and day.'
                        else:
                            response = 'Invalid day entered.'
                    else:
                        response = 'Please enter am or pm.'
                else:
                    response = 'Invalid time, please enter value between 1-12.'
        else:
            form = ReservationForm()
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'Website/displayRoom.html', {'room':room, 'form':form, 'response':response, 'reservation_list':reservation_list})
