# Generated by Django 3.2 on 2023-09-22 19:42

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(choices=[('GENERAL INQUIRY', 'GENERAL INQUIRY'), ('CUSTOMER SUPPORT', 'CUSTOMER SUPPORT'), ('FEEDBACK OR SUGGESTIONS', 'FEEDBACK OR SUGGESTIONS'), ('PARTNERSHIP OR COLLABORATIONS', 'PARTNERSHIP OR COLLABORATIONS')], max_length=30)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('jobtitle', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('BAKU', 'BAKU'), ('SYDNEY', 'SYDNEY'), ('ZURICH', 'ZURICH'), ('TOKYO', 'TOKYO'), ('SAN-FRANCISCO', 'SAN-FRANCISCO')], max_length=50)),
                ('department', models.CharField(choices=[('Product Development and Research', 'Product Development and Research'), ('Marketing and Branding', 'Marketing and Branding'), ('Sales and Distribution', 'Sales and Distribution'), ('Sales and Distribution', 'Sales and Distribution'), ('Finance and Administration', 'Finance and Administration'), ('Research and Analytics', 'Research and Analytics'), ('Creative and Design', 'Creative and Design')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.BigIntegerField()),
                ('number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('coverletter', models.TextField()),
                ('vacancy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='content.vacancies')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
