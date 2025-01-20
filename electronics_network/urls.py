from django.urls import path, include
from rest_framework.routers import DefaultRouter
from electronics_network.views import SupplierViewSet

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]