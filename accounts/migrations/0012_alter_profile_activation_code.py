# Generated by Django 3.2 on 2023-09-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_code',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
