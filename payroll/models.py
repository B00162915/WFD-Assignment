from django.db import models
from employees.models import Employee


class PayrollEntry(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('paid', 'Paid'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    date = models.DateField()

    hoursWorked = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    totalPay = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def calculate_total_pay(self):
        if self.employee.salaryType == 'hourly':
            base = self.hoursWorked * self.employee.hourlyRate
        else:
            base = self.employee.baseSalary

        return base + self.bonus - self.deductions

    def save(self, *args, **kwargs):
        self.totalPay = self.calculate_total_pay()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {self.status}"