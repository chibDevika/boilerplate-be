from pyexpat import model
from rest_framework import serializers
from leavestracker.apps.leaves.models import Leaves

class LeaveSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user.email")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    
    class Meta:
        model = Leaves
        fields = ['employee','started_at','ended_at','reason','email','first_name','last_name']
