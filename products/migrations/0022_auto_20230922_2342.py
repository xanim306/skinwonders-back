# Generated by Django 3.2 on 2023-09-22 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0021_basket_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='basket',
            name='session_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='products.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skintype',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='skintype',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, null=True)),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_option', models.CharField(choices=[('paypal', 'PayPal'), ('credit_card', 'Credit Card')], max_length=20)),
                ('card_number', models.CharField(blank=True, max_length=19, null=True)),
                ('cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='billing_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.billinginfo'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.paymentinfo'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.shippinginfo'),
        ),
    ]
