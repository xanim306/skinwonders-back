import django_filters
from services.choices import LOCATIONS,DEPARTMENTS
from content.models import Vacancies

class VacancyFilter(django_filters.FilterSet):
    jobtitle= django_filters.CharFilter(lookup_expr="icontains")
    location= django_filters.ChoiceFilter(choices=LOCATIONS)
    department= django_filters.ChoiceFilter(choices=DEPARTMENTS)


    class Meta:
        model=Vacancies
        fields=("jobtitle","location","department")

