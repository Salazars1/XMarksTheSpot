from django.shortcuts import render
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
        resListInt = []
        userReservations = len(request.user.reservation_set.all())
        for res in reservation_list:
            resListInt.insert(0, [dayToInt(res), res.time])
        if request.method == 'POST':
            form = ReservationForm(request.POST)
            if userReservations < 3:
                if form.is_valid():
                    dayReserved = form.cleaned_data.get('day')
                    time = form.cleaned_data.get('timeInt')
                    timeType = form.cleaned_data.get('timeType')
                    if time > 0:
                        if form.timeWithTimeType(timeType=timeType) != -1:
                            if timeType == 'pm':
                                if time < 12:
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
                                    return render(request, 'Website/displayRoom.html', {'room':room, 'form':form, 'response':response, 'resListInt':resListInt, 'userReservations':userReservations})

                                else:
                                    response = 'Room already reserved at that time and day.'
                            else:
                                response = 'Invalid day entered.'
                        else:
                            response = 'Please enter am or pm.'
                    else:
                        response = 'Invalid time, please enter value between 1-12.'
            else:
                response = 'Already reached the max amount of reservations.'
        else:
            form = ReservationForm()
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    return render(request, 'Website/displayRoom.html', {'room':room, 'form':form, 'response':response, 'resListInt':resListInt, 'userReservations':userReservations})

def dayToInt(res):
    if res.day == "Monday":
        return 0
    elif res.day == "Tuesday":
        return 1
    elif res.day == "Wednesday":
        return 2
    elif res.day == "Thursday":
        return 3
    elif res.day == "Friday":
        return 4
    elif res.day == "Saturday":
        return 5
    elif res.day == "Sunday":
        return 6
    return -1
