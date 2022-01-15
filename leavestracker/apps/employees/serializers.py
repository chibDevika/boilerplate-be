from rest_framework import serializers
from leavestracker.apps.employees.models import User

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']
