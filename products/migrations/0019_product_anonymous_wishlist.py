# Generated by Django 3.2 on 2023-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='anonymous_wishlist',
            field=models.TextField(blank=True, null=True),
        ),
    ]
