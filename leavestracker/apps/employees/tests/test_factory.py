import factory
from leavestracker.apps.employees.models import CustomUser, Employees

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ('username', 'first_name', 'last_name', 'email')
