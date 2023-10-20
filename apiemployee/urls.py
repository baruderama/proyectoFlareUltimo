from rest_framework import routers
from apiemployee.views import EmployeeViewSet,ContractViewSet,EmployeeContractsViewSet,CreateTokenView,CreateUserView
from django.urls import path, include
router= routers.DefaultRouter()

router.register('api/employees',EmployeeViewSet,'employees')
router.register('api/contract',ContractViewSet,'contracts')


# urlpatterns =router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('api/employees/<int:pk>/contracts/', EmployeeContractsViewSet.as_view(), name='employee-contracts'),
    path('create/', CreateUserView.as_view()),
    path('token/', CreateTokenView.as_view()),
]