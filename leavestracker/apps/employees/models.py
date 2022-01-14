from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class EmployeesModel(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=TRUE)
    updated_time=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
