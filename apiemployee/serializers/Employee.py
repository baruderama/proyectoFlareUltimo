from rest_framework import serializers
# from .models import Contract,Employee
from apiemployee.models import Contract,Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields =('id','name','last_name')