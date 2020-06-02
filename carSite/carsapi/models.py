from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class CarsUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.name
