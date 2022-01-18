from rest_framework import serializers
from leavestracker.apps.leaves.models import Leaves

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = ['employee','started_at','ended_at','reason','email','first_name','last_name']

    def validate(self, attrs):
        instance = Leaves(**attrs)
        instance.clean()
        return attrs
