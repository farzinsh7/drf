from django_filters.rest_framework import FilterSet, NumberFilter
from .models import Product


class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name='unit_price',
                             lookup_expr='gte', label='Minimum Price')
    max_price = NumberFilter(field_name='unit_price',
                             lookup_expr='lte', label='Maximum Price')

    class Meta:
        model = Product
        fields = {
            'collection_id': ['exact'],
        }
