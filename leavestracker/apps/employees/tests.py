from django.test import TestCase
from django.contrib.auth.models import User


class EmployeeTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test-username", firstName="test-name", lastName="test-last-name", email = "abc@gmail.com")
