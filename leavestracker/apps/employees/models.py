from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=TRUE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name