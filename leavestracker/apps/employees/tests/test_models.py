from rest_framework.test import APITestCase
from leavestracker.apps.employees.models import CustomUser, Employees
from leavestracker.apps.employees.tests.test_factory import UserFactory

class TestModels(APITestCase):
    def test_new_user_and_employee_object_creation(self):
        user1 = UserFactory()
        user_qs = CustomUser.objects.filter(id=user1.id).count()
        emp_qs = Employees.objects.filter(user_id=user1.id).count()
        self.assertEquals(user_qs, 1)
        self.assertEquals(emp_qs, 1)

    def test_users_with_same_usernames(self):
        user1 = UserFactory(username='James', first_name='James', last_name='Logan', email='abc@gmail.com')
        try:
            user2 = UserFactory(username='James', first_name='James', last_name='Marshall', email='abcde@gmail.com')
        except ValueError:
            user_qs = CustomUser.objects.filter(username='James').count()
            emp_qs = Employees.objects.filter(user_id=user1.id).count()
            self.assertEquals(user_qs, 1)
            self.assertEquals(emp_qs, 1)
            