from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class CarsUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
