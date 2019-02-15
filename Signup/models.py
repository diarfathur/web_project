from django.db import models
from django.db.models import CharField
from django.db.models import TextField

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=200, default='')
    first_name = models.TextField(max_length=200, default='')
    last_name = models.TextField(max_length=200, default='')
    password = models.CharField(max_length=50, default='')
    confirm_password = models.CharField(max_length=50, default='')
    country = models.TextField(max_length=200, default='')
    address = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.username

