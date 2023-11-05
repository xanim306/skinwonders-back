from django.contrib import admin

# Register your models here.

from .models import ContactUs,Vacancies,CV,Blog


admin.site.register(ContactUs)
admin.site.register(Vacancies)
admin.site.register(CV)
admin.site.register(Blog)


