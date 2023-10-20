from django.db import models
from django.utils import timezone
from apiemployee.models import Employee

class Contract(models.Model):
    start_date=models.DateTimeField(default=timezone.now)
    end_date =models.DateTimeField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)