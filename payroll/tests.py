from django.test import TestCase
from employees.models import Employee
from django.contrib.auth import get_user_model
from .models import PayrollEntry

User = get_user_model()

class PayrollTest(TestCase):

    def test_payroll_calculation(self):
        user = User.objects.create_user(username='emp', password='password', role='coach')

        employee = Employee.objects.create(
            user=user,
            roleType='coach',
            salaryType='hourly',
            hourlyRate=20
        )

        payroll = PayrollEntry.objects.create(
            employee=employee,
            date='2024-01-01',
            hoursWorked=10,
            bonus=50,
            deductions=20
        )

        self.assertEqual(payroll.totalPay, 230)
