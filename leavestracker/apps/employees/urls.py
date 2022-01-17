from django.urls import path
from leavestracker.apps.employees.views import EmployeesView

urlpatterns = [
    path('employees-data/', EmployeesView.as_view(), name="employee-data"),
]
