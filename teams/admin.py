from django.contrib import admin
from .models import Team, Player


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    listDisplay = ('name', 'coach')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    listDisplay = ('user', 'team', 'position')
    listFilter = ('team',)