from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,null=True)