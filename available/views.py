from django.shortcuts import render
from buildings.models import Room, Reservation
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    room_list = Room.objects.order_by('floor__building__name', 'name')
    availableRooms = []
    dayStr = ''
    if now.month == 4:
        today = now.day % 7
        if today == 1:
            dayStr = 'Sunday'
        elif today == 2:
            dayStr = 'Monday'
        elif today == 3:
            dayStr = 'Tuesday'
        elif today == 4:
            dayStr = 'Wednesday'
        elif today == 5:
            dayStr = 'Thursday'
        elif today == 6:
            dayStr = 'Friday'
        elif today == 0:
            dayStr = 'Saturday'
        else:
            dayStr = -1
    for r in room_list:
        available = True
        roomReservations = r.reservation_set.all()
        for re in roomReservations:
            resDay = 0
            if re.day != 24:
                resDay = re.day
            if resDay == dayStr:
                if re.time == now.hour:
                    available = False
        if available:
            availableRooms.insert(len(availableRooms), r)
    context = {'availableRooms': availableRooms}
    return render(request, 'Website/Available.html', context)