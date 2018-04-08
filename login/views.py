from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'registration/login.html')

def createAccount(request):
    response = ''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if '@xavier.edu' in form.cleaned_data.get('email'):
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                request.session['name'] = username
                return redirect('/home/')
            else:
                response = 'Please enter valid Xavier email.'
    else:
        form = CreateUserForm()
    return render(request, 'Website/CreateAccount.html', {'form': form, 'response':response})

