from datetime import datetime, timedelta
from unittest import mock

from leavestracker.apps.leaves import tasks
from leavestracker.apps.leaves.tests.test_factory import LeaveFactory
from leavestracker.apps.employees.tests.test_factory import UserFactory
from leavestracker.apps.employees.models import Employees

from rest_framework.test import APITestCase

class TaskTestCase(APITestCase):
    @mock.patch('leavestracker.apps.leaves.models.Leaves.slack_notification')
    def test_celery_task(self, mock_slack_notification):
        presentday = datetime.now() 
        tomorrow = presentday + timedelta(1)

        user1 = UserFactory(username='Ed', first_name='Edward', last_name='Cullen', email='ed@gmail.com')
        emp1 = Employees.objects.get(user_id = user1.id)
        leave1 = LeaveFactory(employee=emp1, started_at=presentday.strftime('%Y-%m-%d %H:%M'), ended_at=tomorrow.strftime('%Y-%m-%d %H:%M'), reason="Vacation")

        user2 = UserFactory(username='Jake', first_name='Jacob', last_name='Black', email='jake@gmail.com')
        emp2 = Employees.objects.get(user_id = user2.id)
        leave2 = LeaveFactory(employee=emp2, started_at=presentday.strftime('%Y-%m-%d %H:%M'), ended_at=tomorrow.strftime('%Y-%m-%d %H:%M'), reason="Dentist's Appointment")

        response = tasks.Leaves.notify_on_slack_absent_employees()
