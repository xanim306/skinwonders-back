from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from services.generators import CodeGenerator
from services.mixin import DateMixin,SlugMixin
from services.helper import slugify,generate_unique_slug
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from services.choices import STATUS
from accounts.models import Profile

User = get_user_model()

# Create your models here.





def upload_to(instance,filename):
    return f"products/{instance.category.name}/{filename}"


class Category(DateMixin,MPTTModel):
    name = models.CharField(max_length=100,unique=True)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='children')
    slug = models.SlugField(unique=True, editable=False,blank=True,null=True)
    icon = models.ImageField(blank=True,null=True)


    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            self.slug = generate_unique_slug(slug,Category)
        return super().save(*args,**kwargs)

    
    class Meta:
        ordering = ("-created_at", )
        verbose_name = 'Category'
        verbose_name_plural='Categories'





class Product(DateMixin,SlugMixin):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title = models.TextField(blank=True,null=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(editable=False,blank=True,null=True)
    # description = RichTextField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    discount = models.FloatField(blank=True,null=True)
    # wishlist = models.ManyToManyField(User,blank=True)
    sku = models.IntegerField(blank=True,null=True)
    status = models.CharField(choices=STATUS,blank=True,null=True,max_length=300)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at", )
        verbose_name = 'Product'
        verbose_name_plural='Products'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = CodeGenerator.create_products_shortcode(size=10, model_=Product)
        if not self.slug:
            slug = slugify(self.name)
            self.slug = generate_unique_slug(slug,Product)
        return super().save(*args,**kwargs)
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists', null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    session_key = models.CharField(max_length=40,null=True)

    def __str__(self):
        return f"Wishlist for {self.user}"




def upload_to(instance,filename):
    return f"products/{instance.product.name}/{filename}"


class ProductImage(DateMixin):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to=upload_to)

    def __str__(self):
        return self.product.name
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"




# class SkinType(DateMixin):
#     skin = models.CharField(max_length=300,blank=True,null=True)
#     product = models.ManyToManyField(Product,blank=True)

#     def __str__(self):
#         return self.skin



class Newsletter(DateMixin):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.email or "No email"




class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    session_key = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.product.title
    
    class Meta:
        unique_together = [("product","user")]

    @property
    def get_total(self):
        total = self.product.total_price * self.quantity
        return total
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 




class ShippingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)



class BillingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)


class PaymentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    PAYMENT_OPTIONS = (
        ('paypal', 'PayPal'),
        ('credit_card', 'Credit Card'),
    )
    payment_option = models.CharField(max_length=20, choices=PAYMENT_OPTIONS)
    card_number=models.CharField(blank=True,null=True,max_length=19)
    cvv=models.CharField(blank=True,null=True,max_length=3,editable=False)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)



class Order(DateMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('OrderItem', related_name='orders')
    complete = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    shipping_info = models.ForeignKey(ShippingInfo, on_delete=models.SET_NULL, null=True, blank=True)
    billing_info = models.ForeignKey(BillingInfo, on_delete=models.SET_NULL, null=True, blank=True)
    payment_info = models.ForeignKey(PaymentInfo, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40,null=True)



    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    

class OrderItem(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.total_price * self.quantity
        return total





class ProductComment(MPTTModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    parent = TreeForeignKey('self',on_delete = models.CASCADE, blank= True, null = True, related_name = 'children')
    name = models.CharField(max_length=300)
    email = models.EmailField()
    comment = models.TextField()
    session_key = models.CharField(max_length=40,null=True)


    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name
    

