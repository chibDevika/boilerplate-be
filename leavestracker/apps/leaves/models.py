from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.core.exceptions import ValidationError

from leavestracker.apps.common import utils
from leavestracker.apps.employees.models import Employees
from leavestracker.apps.leaves import constants

class Leaves(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    reason = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def clean(self):
        errors = []
        if self.ended_at < self.started_at:
            errors.append(constants.END_DATE_BEFORE_START_DATE)
        
        if not self.id: #for posting new leave
            leaves = Leaves.objects.filter(Q(employee_id = self.employee_id) & (Q(started_at__range = [self.started_at, self.ended_at]) | Q(ended_at__range = [self.started_at, self.ended_at]))).count()
            if not leaves==0:
                errors.append(constants.LEAVE_EXISTS)
        else: #for updating leave
            update_leave = Leaves.objects.filter(Q(employee_id = self.employee_id) & (Q(started_at__range = [self.started_at, self.ended_at]) | Q(ended_at__range = [self.started_at, self.ended_at]))).exclude(id=self.id).count()
            if not update_leave==0:
                errors.append(constants.LEAVE_EXISTS)

        if self.started_at < timezone.now() or self.ended_at < timezone.now():
            errors.append(constants.PAST_DATE)

        if errors:
            raise ValidationError(errors)

    @classmethod
    def absent_employees(cls):
        return cls.objects.filter(Q(started_at__date__lte = timezone.now().date()) & Q(ended_at__date__gte=timezone.now().date()))

    @staticmethod
    def slack_notification(employees):
        message = ""
        for emp in employees.iterator():
            message += (emp.employee.user.first_name + " " + emp.employee.user.last_name + 
                    " email: " + emp.employee.user.email + " (" + emp.started_at.strftime('%Y-%m-%d %H:%M') + 
                    " to " + emp.ended_at.strftime('%Y-%m-%d %H:%M') + "); ")
        utils.slack_notification(message, constants.AFK_SLACK_TITLE)

    @classmethod
    def notify_on_slack_absent_employees(cls):
        employees = cls.absent_employees()
        cls.slack_notification(employees)
