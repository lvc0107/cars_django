from django.db import models
from django.utils.timezone import now


class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
