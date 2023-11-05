from rest_framework import generics
from .serializers import ContactUsSerializer,CVSerializer,VacanciesSerializer,BlogSerializer,BlogDetailSerializer
from ..models import ContactUs,CV,Vacancies,Blog
from django.shortcuts import get_object_or_404,redirect
from rest_framework.response import Response
from .filters import VacancyFilter
from django_filters.rest_framework.backends import DjangoFilterBackend



class ContactUsView(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class VacanciesView(generics.ListAPIView):
    queryset=Vacancies.objects.all()
    serializer_class=VacanciesSerializer
    filter_backends=(DjangoFilterBackend,)
    filterset_class = VacancyFilter



class CVView(generics.CreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

    def perform_create(self, serializer):
        vacancy = get_object_or_404(Vacancies, id=self.kwargs['id'])
        serializer.save(vacancy=vacancy)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)
    

class BlogView(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer



class BlogDetailView(generics.RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogDetailSerializer
    lookup_field="id"