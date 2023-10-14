from django.contrib import admin
from .models import User
from .models import Contract
# Register your models here.
admin.site.register(User)
admin.site.register(Contract)