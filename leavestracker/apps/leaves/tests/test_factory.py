import factory
from leavestracker.apps.leaves.models import Leaves

class LeaveFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Leaves
        django_get_or_create = ('employee', 'started_at', 'ended_at', 'reason')

