from django.db import models



class DateMixin(models.Model):
    created_at = models.DateField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateField(auto_now=True,blank=True,null=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    code = models.SlugField(unique=True, editable=False,blank=True,null=True)
    sku  = models.SlugField(unique=True, editable=False,blank=True,null=True)

    class Meta:
        abstract = True