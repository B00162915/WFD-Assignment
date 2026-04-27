from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Employee(models.Model):
    ROLE_TYPE_CHOICES = (
        ('coach', 'Coach'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin Staff'),
    )

    SALARY_TYPE_CHOICES = (
        ('fixed', 'Fixed Salary'),
        ('hourly', 'Hourly Rate'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    roleType = models.CharField(max_length=20, choices=ROLE_TYPE_CHOICES)
    salaryType = models.CharField(max_length=10, choices=SALARY_TYPE_CHOICES)

    baseSalary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hourlyRate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    dateHired = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.roleType}"