from django.db.models import Q
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse

from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.employees.models import CustomUser, Employees
from leavestracker.apps.employees.tests.test_factory import UserFactory
from leavestracker.apps.leaves.tests.test_factory import LeaveFactory

class TestViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('leaves')
    
    def test_new_leave(self):
        new_user = UserFactory(username = 'john', first_name = 'john', last_name = 'john', email = 'john@gmail.com')
        self.client.force_authenticate(user=new_user)
        new_emp = Employees.objects.get(user_id=new_user.id)

        data = {
            'employee': new_emp.id,
            'started_at': '2022-02-25',
            'ended_at': '2022-02-26',
            'reason': '',
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)

    def test_leave_exists(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)

        old_leave = LeaveFactory(employee=emp, started_at="2023-01-25", ended_at="2023-01-27", reason="out of station")
        data = {
            'employee': emp,
            'started_at': '2023-01-23',
            'ended_at': '2023-01-25',
            'reason': 'vacation',
        }
        response = self.client.post(self.url, data)
        self.assertNotEquals(response.status_code, 200)
        new_leave = Leaves.objects.filter(reason = "vacation").count()
        self.assertEquals(new_leave, 0)

    def test_invalid_dates(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        self.client.force_authenticate(user=user)
        emp = Employees.objects.get(user_id = user.id)
        data = {
            'employee': emp,
            'started_at': '2022-02-28',
            'ended_at': '2022-02-29',
            'reason': 'vacation',
        }
        response = self.client.post(self.url, data)
        count = Leaves.objects.filter(employee = emp).count()
        self.assertEquals(count, 0)
        self.assertNotEquals(response.status_code, 200)


    def test_past_dates(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)
        data = {
            'employee': emp,
            'started_at': '2021-02-23',
            'ended_at': '2022-02-19',
            'reason': 'vacation',
        }
        response = self.client.post(self.url, data)
        count = Leaves.objects.filter(employee = emp).count()
        self.assertEquals(count, 0)
        self.assertNotEquals(response.status_code, 200)

    def test_get_leave(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)

        leave_new = LeaveFactory(employee=emp, started_at="2022-03-01", ended_at="2022-03-06",reason="")
        id = leave_new.id
        url = reverse('leaves', args=[id])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['employee'], emp.id)


    def test_get_leave_does_not_exist(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)

        url = reverse('leaves', args=[10000000])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 400)
        

    def test_update_leave(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)

        old_leave = LeaveFactory(employee=emp, started_at="2023-01-25", ended_at="2023-01-27", reason="out of station")
        leave_id = old_leave.id
        url = reverse('leaves', args=[leave_id])
        data = {
            'started_at': '2023-01-24',
            'ended_at': '2023-01-27',
            'reason': 'surgery',
        }
        response = self.client.patch(url, data)
        self.assertEquals(response.status_code, 200)
        leaves_updated = Leaves.objects.filter(reason='surgery').count()
        self.assertEquals(leaves_updated, 1)
        leave_previous = leaves_updated = Leaves.objects.filter(reason='out of station').count()
        self.assertEquals(leave_previous, 0)

    def update_leave_does_not_exist(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        self.client.force_authenticate(user=user)

        url = reverse('leaves', args=[100000])
        data = {
            'started_at': '2023-01-24',
            'ended_at': '2023-01-27',
            'reason': 'birthday',
        }
        response = self.client.patch(url, data)
        self.assertEquals(response.status_code, 400)


    