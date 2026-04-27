from django.contrib import admin
from .models import PayrollEntry

@admin.register(PayrollEntry)
class PayrollAdmin(admin.ModelAdmin):
    listDisplay = ('employee', 'date', 'totalPay', 'status')
    listFilter = ('status',)