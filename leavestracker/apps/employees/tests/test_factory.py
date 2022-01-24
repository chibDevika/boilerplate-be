import factory
from leavestracker.apps.employees.models import CustomUser

class UserFactory(factory.django.DjangoModelFactory):
    username='Claire'
    first_name='Claire'
    last_name='Dunphy'
    email='sample@gmail.com'

    class Meta:
        model = CustomUser
