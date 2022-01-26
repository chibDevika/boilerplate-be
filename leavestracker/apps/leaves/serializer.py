from leavestracker.apps.leaves.models import Leaves
from rest_framework import serializers

class LeaveSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="employee.user.first_name")
    last_name = serializers.ReadOnlyField(source="employee.user.last_name")
    email = serializers.ReadOnlyField(source="employee.user.email")

    class Meta:
        model = Leaves
        fields = ['employee','id','started_at','ended_at','reason','first_name','last_name','email']

    def validate(self, attrs):
        instance = Leaves(**attrs)
        instance.clean()
        return attrs
