from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.id

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        if self.id:
            Employees.objects.create(user = self)


class Employees(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id
