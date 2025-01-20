from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from electronics_network.models import Supplier
from electronics_network.serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        country = self.request.query_params.get('country', None)
        queryset = Supplier.objects.all()
        if country:
            queryset = queryset.filter(country=country)
        return queryset

    @action(detail=True, methods=['post'])
    def clear_debt(self, request, pk=None):
        supplier = self.get_object()
        supplier.debt = 0
        supplier.save()
        return Response({'message': 'Долг успешно очищен'})