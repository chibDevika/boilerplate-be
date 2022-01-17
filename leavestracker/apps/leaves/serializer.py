from rest_framework import serializers
from leavestracker.apps.leaves.models import Leaves

class LeaveSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source="user.email")
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    
    class Meta:
        model = Leaves
        fields = ['employee','started_at','ended_at','reason','email','first_name','last_name']


    # def validate(self, data):
    #     if data['started_at'] > data['ended_at']:
    #         raise serializers.ValidationError("You can't update this date as this date has passed.")

    def validate_is_active(self,value):
        if self.is_active==True:
            raise serializers.ValidationError("A leave already exists on this date.")
        return value

    # # def validate_created_

    #     if self.created_at>self.ended_at:
    #         raise ValidationError("End date of a leave can't be before the start date.")