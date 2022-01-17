from django.core.exceptions import ValidationError
from datetime import datetime

def validate_date(self, value):
    if value<=datetime.now:
        raise ValidationError("You can't update this date as this date has passed.")
    
    elif self.is_active == True:
        raise ValidationError("A leave already exists on this date.")

def validate_end_date(self,value):
    if self.created_at > value:
        raise ValidationError("End date of a leave can't be before the start date.")