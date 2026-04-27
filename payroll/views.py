from django.shortcuts import render, redirect, get_object_or_404
from .models import PayrollEntry
from .forms import PayrollForm
from django.http import HttpResponseForbidden


def payrollList(request):
    payrolls = PayrollEntry.objects.all()
    return render(request, 'payroll/list.html', {'payrolls': payrolls})


def payrollCreate(request):
    if (request.user.role == 'finance' or request.user.role == 'manager') == False:
        return HttpResponseForbidden("Not allowed")
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payrollList')
    else:
        form = PayrollForm()

    return render(request, 'payroll/create.html', {'form': form})


def payrollApprove(request, pk):
    payroll = get_object_or_404(PayrollEntry, pk=pk)
    payroll.status = 'approved'
    payroll.save()
    return redirect('payroll_list')


def payrollPay(request, pk):
    payroll = get_object_or_404(PayrollEntry, pk=pk)
    payroll.status = 'paid'
    payroll.save()
    return redirect('payrollList')