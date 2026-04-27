from django.test import TestCase
from teams.models import Team
from employees.models import Employee
from django.contrib.auth import get_user_model
from .models import TrainingSession

User = get_user_model()


class TrainingTest(TestCase):

    def testCreateSession(self):
        user = User.objects.create_user(username='coach1', password='password', role='coach')

        employee = Employee.objects.create(
            user=user,
            roleType='coach',
            salaryType='fixed',
            baseSalary=3000
        )

        team = Team.objects.create(name='Team A', coach=employee)

        session = TrainingSession.objects.create(
            team=team,
            coach=employee,
            date='2024-01-01',
            duration=2
        )

        self.assertEqual(session.team.name, 'Team A')
