from django.db import models
from django.db.models import Q
from leavestracker.apps.employees.models import Employees
from django.core.exceptions import ValidationError
from leavestracker.apps.leaves import constants
from django.utils import timezone


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
            errors.append(constants.END_DATE_BEFORE_START_DATE)
        
        leaves = Leaves.objects.filter(Q(started_at__range = [self.started_at, self.ended_at]) | Q(ended_at__range = [self.started_at, self.ended_at])).count()
        if not leaves==0:
            errors.append(constants.LEAVE_EXISTS)

        if self.started_at < timezone.now() or self.ended_at < timezone.now():
            errors.append(constants.PAST_DATE)

        raise ValidationError(errors)
