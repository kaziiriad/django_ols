import django_filters
from ..models import Course


class CourseFilterSet(django_filters.FilterSet):

    class Meta:
        model = Course
        fields = ['instructor', 'duration_minutes', 'price_bdt']
