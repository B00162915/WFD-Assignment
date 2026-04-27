from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Employee

User = get_user_model()

class EmployeeTest(TestCase):

    def testCreateEmployee(self):
        user = User.objects.create_user(
            username='emp1',
            password='password',
            role='coach'
        )

        employee = Employee.objects.create(
            user=user,
            role_type='coach',
            salary_type='hourly',
            hourly_rate=20
        )

        self.assertEqual(employee.roleType, 'coach')