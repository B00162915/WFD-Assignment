from django.test import TestCase
from django.contrib.auth import get_user_model
from employees.models import Employee
from .models import Team

User = get_user_model()


class TeamTest(TestCase):

    def testCreateTeam(self):
        user = User.objects.create_user(username='coach1', password='password', role='coach')

        employee = Employee.objects.create(
            user=user,
            roleType='coach',
            salaryType='fixed',
            baseSalary=3000
        )

        team = Team.objects.create(name='Team A', coach=employee)

        self.assertEqual(team.name, 'Team A')
