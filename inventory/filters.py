import django_filters
from .models import Stock    
from django.db.models import Q

class StockFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Stock
        fields = []

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(sku__icontains=value)
        )