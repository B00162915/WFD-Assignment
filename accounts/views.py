from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.http import HttpResponseForbidden

# Create your views here.

def registerView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return redirect('login')

def managerOnlyView(request):
    if request.user.role != 'manager':
        return HttpResponseForbidden('No Entry Allowed.')
    
    return render(request, 'manager.html')