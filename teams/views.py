from django.shortcuts import render, redirect
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.http import HttpResponseForbidden


def teamList(request):
    teams = Team.objects.all()
    return render(request, 'teams/teamList.html', {'teams': teams})


def teamCreate(request):
    if request.user.role == 'finance' or request.user.role == 'manager':
        return HttpResponseForbidden("Permission Denied")
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teamList')
    else:
        form = TeamForm()

    return render(request, 'teams/teamCreate.html', {'form': form})


def playerList(request):
    players = Player.objects.all()
    return render(request, 'teams/playerList.html', {'players': players})


def playerCreate(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playerList')
    else:
        form = PlayerForm()

    return render(request, 'teams/playerCreate.html', {'form': form})