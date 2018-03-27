from django.shortcuts import render
from buildings.models import Building, Floor, Room

# Create your views here.
def index(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'Website/Available.html', context)