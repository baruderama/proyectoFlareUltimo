from apiemployee.models import Employee,Contract
from rest_framework import viewsets,permissions,generics,authentication
from apiemployee.serializers import EmployeeSerializer,ContractSerializer,UserSerializer,AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.response import Response

class CreateUserView(generics.CreateAPIView):
    serializer_class=UserSerializer
    
class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerializer