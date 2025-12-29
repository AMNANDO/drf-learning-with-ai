import django_filters
from .models import Profile

class ProfileFilter(django_filters.FilterSet):
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')
    class Meta:
        model = Profile
        fields = {'age'}