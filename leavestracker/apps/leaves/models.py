from django.db import models
from leavestracker.apps.employees.models import Employees
from django.core.exceptions import ValidationError
from datetime import datetime


class Leaves(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    reason = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
