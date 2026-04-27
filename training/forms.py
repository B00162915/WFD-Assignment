from django import forms
from .models import TrainingSession, Attendance


class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = '__all__'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'