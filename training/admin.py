from django.contrib import admin
from .models import TrainingSession, Attendance


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    listDisplay = ('team', 'coach', 'date', 'duration')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    listDisplay = ('session', 'player', 'present')
    listFilter = ('session',)