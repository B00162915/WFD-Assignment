from django.shortcuts import render, redirect
from .models import TrainingSession, Attendance
from .forms import TrainingSessionForm, AttendanceForm
from django.http import HttpResponseForbidden


def sessionList(request):
    sessions = TrainingSession.objects.all()
    return render(request, 'training/sessionList.html', {'sessions': sessions})


def sessionCreate(request):
    if request.user.role == 'coach' or request.user.role == 'manager':
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessionList')
    else:
        form = TrainingSessionForm()

    return render(request, 'training/sessionCreate.html', {'form': form})


def attendanceCreate(request):
    if request.user.role == 'coach' or request.user.role == 'manager':
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessionList')
    else:
        form = AttendanceForm()

    return render(request, 'training/attendanceCreate.html', {'form': form})