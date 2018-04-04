from django.shortcuts import render

# Create your views here.
def index(request):
    reservationList = request.user.reservation_set.order_by('day', 'time', 'room')
    context = {'user' : request.user, 'reservationList':reservationList}
    return render(request, 'Website/profile.html', context)