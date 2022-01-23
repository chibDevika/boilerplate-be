from rest_framework.test import APITestCase
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves.tests.test_factory import LeaveFactory
from leavestracker.apps.employees.models import CustomUser, Employees
from leavestracker.apps.employees.tests.test_factory import UserFactory

class TestModels(APITestCase):
    def test_create_new_leave_object(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        leave = LeaveFactory(employee=emp, started_at="2022-02-24", ended_at="2022-02-26", reason="holiday")
        leave_qs = Leaves.objects.get(employee_id=emp.id)
        self.assertEquals(leave_qs.id, 1)




