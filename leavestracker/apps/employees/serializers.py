from rest_framework import serializers
from leavestracker.apps.employees.models import CustomUser

class EmployeesSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="employees.id")

    class Meta:
        model = CustomUser
        fields = ['id','first_name', 'last_name', 'email','username']