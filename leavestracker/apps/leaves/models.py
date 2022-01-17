from django.db import models
from leavestracker.apps.employees.models import Employees
from django.core.exceptions import ValidationError
from datetime import datetime


class Leaves(models.Model):
    def validate_date(self, value):
        if value<=datetime.now:
            raise ValidationError("You can't update this date as this date has passed.")
        
        elif self.is_active == True:
            raise ValidationError("A leave already exists on this date.")

    def validate_end_date(self,value):
        if self.created_at > value:
            raise ValidationError("End date of a leave can't be before the start date.")

    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    started_at = models.DateTimeField(validators=[validate_date])
    ended_at = models.DateField(validators=[validate_date, validate_end_date])
    reason = models.TextField
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
