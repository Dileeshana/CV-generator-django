import django_filters
from django_filters import CharFilter
from .models import *


class CvFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    nic = CharFilter(field_name='nic', lookup_expr='icontains')
    class Meta:
        model = Cvdetails
        fields = ['first_name' , 'nic']