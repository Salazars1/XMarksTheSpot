from django.shortcuts import render, redirect
from .forms import UserUpdate
from django.contrib.auth.models import User
from django.db import IntegrityError

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
            if form.cleaned_data.get('username'):
                newUsername = form.cleaned_data.get('username')
            if form.cleaned_data.get('first_name'):
                newFirstName = form.cleaned_data.get('first_name')
            if form.cleaned_data.get('last_name'):
                newLastName = form.cleaned_data.get('last_name')
            if form.cleaned_data.get('email'):
                newEmail = form.cleaned_data.get('email')
            try:
                user.username = newUsername
                user.first_name = newFirstName
                user.last_name = newLastName
                user.email = newEmail
                user.save()
                return redirect('/profile')
            except IntegrityError:
                response = 'Username already in use.'
                form = UserUpdate()
    else:
        form = UserUpdate()
    return render(request, 'Website/edit.html', {'form': form, 'response':response})