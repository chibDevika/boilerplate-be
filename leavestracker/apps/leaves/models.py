from django.db import models
from django.db.models import Q
from leavestracker.apps.employees.models import Employees
from django.core.exceptions import ValidationError
from datetime import datetime
from leavestracker.apps.leaves import constants
import pytz


class Leaves(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    reason = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def clean(self):
        errors = []
        if self.ended_at < self.started_at:
            errors.append(constants.end_date_before_start_date)
        
        leaves = Leaves.objects.filter(Q(started_at__range = [self.started_at, self.ended_at]) | Q(ended_at__range = [self.started_at, self.ended_at])).first()
        if leaves==None:
                pass
        else:
            errors.append(constants.leave_exists)

        now = pytz.utc.localize(datetime.now())
        if self.started_at < now or self.ended_at < now:
            errors.append(constants.past_date)

        raise ValidationError(errors)

