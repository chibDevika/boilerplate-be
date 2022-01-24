import factory

from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.employees.tests.test_factory import UserFactory

class LeaveFactory(factory.django.DjangoModelFactory):
    employee = factory.SubFactory(UserFactory)
    started_at = "2025-01-01"
    ended_at = "2025-01-02"
    reason = "Holiday"

    class Meta:
        model = Leaves
