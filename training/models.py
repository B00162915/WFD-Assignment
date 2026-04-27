from django.db import models
from teams.models import Team, Player
from employees.models import Employee


class TrainingSession(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    coach = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'roleType': 'coach'}
    )

    date = models.DateField()
    duration = models.DecimalField(max_digits=4, decimal_places=2)  # hours

    def __str__(self):
        return f"{self.team.name} - {self.date}"


class Attendance(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='attendances')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.player.user.username} - {self.session.date}"