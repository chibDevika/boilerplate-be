from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from leavestracker.apps.employees.models import Employees
 
 
@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employees.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_employee(sender, instance, created, **kwargs):
        if created == False:
            instance.employees.save()
