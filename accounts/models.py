from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField
from services.generators import CodeGenerator
from services.helper import slugify, generate_unique_slug


class MyUserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_active=True, is_staff=False, is_superuser=False
    ):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# def upload_to(instance,filename):
#     return f'users/{instance.slug}/{filename}'


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True,)
    surname = models.CharField(max_length=40, blank=True, null=True)
    mobile = PhoneNumberField(blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True, null=True,editable=False)
    age = models.BigIntegerField(blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    # image = models.ImageField(blank=True, null=True)


    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "MyUser"
        verbose_name_plural = "MyUser"

    def __str__(self):
        return self.email
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = CodeGenerator.create_user_slug_code(size=15, model_=MyUser)

        return super(MyUser, self).save(*args, **kwargs)
    


class Profile(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    activation_code = models.PositiveBigIntegerField(blank=True,null=True,unique=True)


    def __str__(self):
        return self.user.email

