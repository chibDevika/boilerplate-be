from django.db import models
from leavestracker.apps.employees.models import Employees
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz


class Leaves(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    reason = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def first_name(self):
        return self.employee.user.first_name
    
    def last_name(self):
        return self.employee.user.last_name

    def email(self):
        return self.employee.user.email

    def clean(self):
        if self.ended_at < self.started_at:
            raise ValidationError("End date of a leave can't be before the start date.")
        
        def get_queryset_startdate(self):
            leaves = Leaves.objects.filter(started_at__range = [self.started_at, self.ended_at]).first()
            if leaves==None:
                pass
            else:
                raise ValidationError("A leave already exists in this interval. You may delete the previous entry or change your new dates")
            
        def get_queryset_enddate(self):
            leaves = Leaves.objects.filter(ended_atrange = [self.started_at, self.ended_at]).first()
            if leaves==None:
                pass
            else:
                raise ValidationError("A leave already exists in this interval. You may delete the previous entry or change your new dates")

        get_queryset_startdate(self)
        get_queryset_enddate(self)

        now = pytz.utc.localize(datetime.now())
        if self.started_at < now:
            raise ValidationError("You can't create a leave on this date or update this date as this date has passed.")

        if self.ended_at < now:
            raise ValidationError("You can't create a leave on this date or update this date as this date has passed.")
