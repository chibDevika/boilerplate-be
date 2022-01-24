import factory

from datetime import datetime, timedelta
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.employees.tests.test_factory import UserFactory
from leavestracker.apps.employees.models import Employees

class LeaveFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Leaves
        django_get_or_create = ('employee', 'started_at', 'ended_at', 'reason')
