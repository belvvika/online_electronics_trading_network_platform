from rest_framework import serializers
from electronics_network.models import Supplier, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'level', 'debt', 'supplier_name', 'create_time', 'products']

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
