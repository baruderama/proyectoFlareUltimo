from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('Falta email')
        user =self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_staff =True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    name =models.CharField(max_length=255)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    
    objects=UserManager()
    
    USERNAME_FIELD='email'
    

class Employee(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100,null=True)
    
    
class Contract(models.Model):
    start_date=models.DateTimeField(default=timezone.now)
    end_date =models.DateTimeField(null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    