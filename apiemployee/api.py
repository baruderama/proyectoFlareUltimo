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
    
class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = ContractSerializer
    
class EmployeeContractsViewSet(generics.ListAPIView):
    serializer_class = ContractSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        employee_id = self.kwargs['pk']  
        return Contract.objects.filter(employee=employee_id)
    
class CreateUserView(generics.CreateAPIView):
    serializer_class=UserSerializer
    
class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerializer