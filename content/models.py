from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

from services.mixin import DateMixin
# Create your models here.
from services.choices import SUBJECTS,LOCATIONS,DEPARTMENTS,TYPE,DATE

class ContactUs(DateMixin):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30,choices=SUBJECTS)
    message = models.TextField()

    class Meta:
        ordering = ("-created_at", )
        verbose_name = 'Contact'
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.email
    


class Vacancies(DateMixin):
    jobtitle=models.CharField(max_length=100)
    location = models.CharField(max_length=50,choices=LOCATIONS)
    department =models.CharField(max_length=50,choices=DEPARTMENTS)

    def __str__(self):
        return self.jobtitle


class CV(DateMixin):
    vacancy = models.ForeignKey(Vacancies,blank=True,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    age = models.BigIntegerField()
    number=PhoneNumberField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    coverletter=models.TextField()

    def __str__(self):
        return f"{self.fullname}-->{self.vacancy}"


def upload_to(instance,filename):
    return f"blogs/{instance.title}/{filename}"

class Blog(DateMixin):
    title = models.CharField(max_length=300)
    description = RichTextField()
    type = models.CharField(choices=TYPE,max_length=50)
    image = models.ImageField(blank=True,null=True)
    date = models.CharField(choices=DATE,max_length=50)

    def __str__(self):
        return self.title