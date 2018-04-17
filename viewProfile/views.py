from django.shortcuts import render, redirect
from .forms import UserUpdate
from django.contrib.auth.models import User
from django.db import IntegrityError
from buildings.models import Reservation
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    if not request.user.username:
        return redirect('login')
    reservationList = request.user.reservation_set.order_by('day', 'time', 'room')
    context = {'user' : request.user, 'reservationList':reservationList}
    return render(request, 'Website/profile.html', context)

def editAccount(request):
    if not request.user.username:
        return redirect('login')
    response = ''
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        form = UserUpdate(request.POST)
        if form.is_valid():
            newUsername = user.username
            newFirstName = user.first_name
            newLastName = user.last_name
            newEmail = user.email
            tempEmail = form.cleaned_data.get('email')
            if form.cleaned_data.get('username'):
                newUsername = form.cleaned_data.get('username')
            if form.cleaned_data.get('first_name'):
                newFirstName = form.cleaned_data.get('first_name')
            if form.cleaned_data.get('last_name'):
                newLastName = form.cleaned_data.get('last_name')
            emailUsed = False
            if form.cleaned_data.get('email'):
                userList = User.objects.all()
                i = 0
                while i < len(userList) and not emailUsed:
                    if userList[i].email == tempEmail:
                        emailUsed = True
                    i += 1
                if not emailUsed:
                    if '@xavier.edu' in tempEmail:
                        newEmail = tempEmail
                        try:
                            user.username = newUsername
                            user.first_name = newFirstName
                            user.last_name = newLastName
                            user.email = newEmail
                            user.save()
                            return redirect('/profile')
                        except IntegrityError:
                            response = 'Username already in use.'
                    else:
                        response = 'Invalid email.'
                else:
                    response = 'Email already in use.'
            else:
                try:
                    user.username = newUsername
                    user.first_name = newFirstName
                    user.last_name = newLastName
                    user.email = newEmail
                    user.save()
                    return redirect('/profile')
                except IntegrityError:
                    response = 'Username already in use.'
    else:
        form = UserUpdate()
    return render(request, 'Website/edit.html', {'form': form, 'response':response})

def cancelReservation(request, id):
    if request.method == 'POST':
        Reservation.objects.get(pk=id).delete()
        return redirect('/profile')
    return render(request, 'Website/confirmation.html', {'reservation':Reservation.objects.get(pk=id)})

def checkIn(request, id):
    reservation = Reservation.objects.get(pk=id)
    if request.method == 'POST':
        reservation.checkedIn = True
        reservation.save()
        return redirect('/profile')
    else:
        now = datetime.datetime.now()
        time = reservation.time
        if time == 24:
            time = 0
        if reservation.day == now.strftime("%A") and not reservation.checkedIn:
            if (time == now.hour and now.minute <= 10) or (time - 1 == now.hour and now.minute >= 50):
                return render(request, 'Website/checkIn.html', {'reservation': reservation})
        return render(request, 'Website/checkInFail.html', {'r': reservation})