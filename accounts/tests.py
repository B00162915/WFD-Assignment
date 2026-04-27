from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTest(TestCase):

    def testCreateUser(self):
        user = User.objects.create_user(
            username='testuser',
            password='password',
            role='manager'
        )
        self.assertEqual(user.role, 'manager')