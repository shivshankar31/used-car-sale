# Generated by Django 4.0.2 on 2022-03-14 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_doors_alter_car_fuel_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
    ]
