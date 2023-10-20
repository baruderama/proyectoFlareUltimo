from rest_framework import serializers
# from .models import Contract,Employee
from apiemployee.models import Contract,Employee

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contract
        fields =('id','start_date','employee','end_date')