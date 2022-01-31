from leavestracker.apps.leaves.models import Leaves
from rest_framework import serializers

class LeaveSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source="employee.user.first_name")
    last_name = serializers.ReadOnlyField(source="employee.user.last_name")
    email = serializers.ReadOnlyField(source="employee.user.email")

    class Meta:
        model = Leaves
        fields = ['employee','id','started_at','ended_at','reason','first_name','last_name','email','is_active']

    def validate(self, attrs):
        instance = Leaves(**attrs)
        if(self.instance):
            instance.id = self.instance.id
            instance.started_at = attrs['started_at']
            instance.ended_at = attrs['ended_at']
            instance.reason = attrs['reason']
        instance.clean()
        return attrs
