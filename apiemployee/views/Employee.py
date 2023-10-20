from apiemployee.models import Employee,Contract
from rest_framework import viewsets,permissions,generics,authentication
from apiemployee.serializers import EmployeeSerializer,ContractSerializer,UserSerializer,AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = EmployeeSerializer