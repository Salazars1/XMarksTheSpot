from django.shortcuts import render
from buildings.models import Room
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    room_list = Room.objects.order_by('floor__building__name', 'name')
    context = {'room_list': room_list}
    return render(request, 'Website/Available.html', context)