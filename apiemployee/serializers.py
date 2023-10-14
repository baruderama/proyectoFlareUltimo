from rest_framework import serializers
from .models import Contract,Employee
from django.contrib.auth import get_user_model,authenticate

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields =('id','name','last_name')

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contract
        fields =('id','start_date','employee','end_date')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =['email','password','name']
        extra_kwargs ={'password':{'write_only':True}}
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
class AuthTokenSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password= serializers.CharField(style={'input_type':'password'})
    
    def validate(self, data):
        email =data.get('email')
        password= data.get('password')
        user =authenticate(
            request= self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            raise serializers.ValidationError('No se puedo autenticar', code='authorization')
        
        data['user']=user
        return data