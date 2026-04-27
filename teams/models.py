from django.db import models
from django.conf import settings
from employees.models import Employee

User = settings.AUTH_USER_MODEL


class Team(models.Model):
    name = models.CharField(max_length=100)

    coach = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'roleType': 'coach'}
    )

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = (
        ('forward', 'Forward'),
        ('midfielder', 'Midfielder'),
        ('defender', 'Defender'),
        ('goalkeeper', 'Goalkeeper'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    performance_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.team.name}"