from django import forms
from .models import PayrollEntry

class PayrollForm(forms.ModelForm):
    class Meta:
        model = PayrollEntry
        fields = ['employee', 'date', 'hoursWorked', 'bonus', 'deductions']