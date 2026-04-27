from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


def employeeList(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


def employeeCreate(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employeeList')
    else:
        form = EmployeeForm()

    return render(request, 'employees/create.html', {'form': form})