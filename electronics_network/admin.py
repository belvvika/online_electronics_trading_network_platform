from django.contrib import admin
from electronics_network.models import Supplier, Product

class CityFilter(admin.SimpleListFilter):
    title = 'город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = set(Supplier.objects.values_list('city', flat=True))
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(city=self.value())
        return queryset


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'level', 'debt', 'create_time')
    list_filter = ('country', 'level', CityFilter)
    search_fields = ('name', 'city')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date_release', 'supplier')
    list_filter = ('supplier',)
    search_fields = ('name', 'model')
