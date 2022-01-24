from datetime import datetime, timedelta

from rest_framework.test import APITestCase
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves.tests.test_factory import LeaveFactory
from leavestracker.apps.employees.models import Employees
from leavestracker.apps.employees.tests.test_factory import UserFactory

class TestModels(APITestCase):
    def test_create_new_leave_object(self):
        user = UserFactory(username='Claire', first_name='Claire', last_name='Dunphy', email='sample@gmail.com')
        emp = Employees.objects.get(user_id = user.id)
        leave = LeaveFactory(employee=emp, started_at="2022-02-24", ended_at="2022-02-26", reason="holiday")
        leave_qs = Leaves.objects.get(employee_id=emp.id)
        self.assertEquals(leave_qs.id, 1)

    def test_model_query(self):
        presentday = datetime.now() 
        tomorrow = presentday + timedelta(1)
        dayAfterTomorrow = tomorrow + timedelta(1)
        yesterday = presentday - timedelta(1)
        dayBeforeYesterday = yesterday - timedelta(1)

        user1 = UserFactory(username='Ed', first_name='Edward', last_name='Cullen', email='ed@gmail.com')
        emp1 = Employees.objects.get(user_id=user1.id)
        leave1 = LeaveFactory(employee=emp1, started_at=presentday.strftime('%Y-%m-%d'), ended_at=tomorrow.strftime('%Y-%m-%d'), reason="Vacation")

        user2 = UserFactory(username='Jake', first_name='Jacob', last_name='Black', email='jake@gmail.com')
        emp2 = Employees.objects.get(user_id=user2.id)

        leave4 = LeaveFactory(employee=emp1, started_at=dayBeforeYesterday.strftime('%Y-%m-%d'), ended_at=yesterday.strftime('%Y-%m-%d'), reason="Dentist's Appointment")
        leave2 = LeaveFactory(employee=emp1, started_at=tomorrow.strftime('%Y-%m-%d'), ended_at=dayAfterTomorrow.strftime('%Y-%m-%d'), reason="Dentist's Appointment")
        leave3 = LeaveFactory(employee=emp2, started_at=presentday.strftime('%Y-%m-%d'), ended_at=tomorrow.strftime('%Y-%m-%d'), reason="Dentist's Appointment")

        response = Leaves.absent_employees()
        actual_response = []
        for value in response:
            actual_response.append(value)
        
        self.assertEquals(actual_response, [leave1, leave3])




