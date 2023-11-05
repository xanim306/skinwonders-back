from django.urls import path
from . import views

app_name='content-api'

urlpatterns = [
    path('contactus/',views.ContactUsView.as_view(),name='contactus'),
    path('vacancies/',views.VacanciesView.as_view(),name='vacancies'),
    path('apply/job/<int:id>/',views.CVView.as_view(),name='apply-job'),
    path('blogs/',views.BlogView.as_view(),name='blogs'),
    path('blog/<int:id>/',views.BlogDetailView.as_view(),name='blog'),

]
