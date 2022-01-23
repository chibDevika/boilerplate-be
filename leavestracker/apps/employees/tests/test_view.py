from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from leavestracker. apps.employees.models import CustomUser, Employees
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
        user = UserFactory(username='Jason', first_name='Jason', last_name='Holden',email='abc@gmail.com')
        data = {
            'username' : 'Jason',
            'first_name':'jason',
            'last_name':'mraz',
            'email':'abcd@gmail.com'
        }
        response = self.client.post(self.post_url, data)
        user = CustomUser.objects.filter(username="Jason").count()
        self.assertEquals(user, 1) 
        self.assertEquals(response.status_code, 200)
        

