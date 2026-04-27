from django import forms
from .models import Team, Player


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'