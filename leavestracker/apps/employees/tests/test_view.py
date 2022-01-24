from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from leavestracker. apps.employees.models import CustomUser
from leavestracker.apps.employees.tests.test_factory import UserFactory

class TestViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.post_url = reverse('employee')


    def test_new_user(self):
        data = {
            'username': 'Brenda',
            'first_name':'Brenda',
            'last_name':'Olive',
            'email':'brenda@gmail.com'
        }
        response = self.client.post(self.post_url, data)
        self.assertEquals
        user_qs = CustomUser.objects.filter(username='Brenda').count()
        self.assertEquals(user_qs,1)

    def test_existing_user(self):
        user = UserFactory()
        data = {
            'username' : user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        response = self.client.post(self.post_url, data)
        user = CustomUser.objects.filter(username=user.username).count()
        self.assertEquals(user, 1) 
        self.assertEquals(response.status_code, 200)
        