# Generated by Django 3.2 on 2023-09-03 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230903_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='code',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sku',
        ),
    ]
