from django.shortcuts import render
from buildings.models import Room, Reservation
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    room_list = Room.objects.order_by('floor__building__name', 'name')
    availableRooms = []
    dayStr = ''
    dayStr = now.strftime("%A")
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