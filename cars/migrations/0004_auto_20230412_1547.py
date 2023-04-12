# Generated by Django 3.0.7 on 2023-04-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20230412_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(choices=[('Bus', 'Bus'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Mini-Van', 'Mini-Van'), ('Offroad', 'Offroad'), ('Pickup', 'Pickup'), ('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Truck', 'Truck'), ('Van', 'Van'), ('Wagon', 'Wagon'), ('Others', 'Others')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Fair', 'Fair'), ('Good', 'Good'), ('Like New', 'Like New'), ('New', 'New'), ('Salvage', 'Salvage')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(choices=[('3 Cylinders', '3 Cylinders'), ('4 Cylinders', '4 Cylinders'), ('5 Cylinders', '5 Cylinders'), ('6 Cylinders', '6 Cylinders'), ('8 Cylinders', '8 Cylinders'), ('10 Cylinders', '10 Cylinders'), ('12 Cylinders', '12 Cylinders'), ('Other Cylinders', 'Other Cylinders')], max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Gas', 'Gas'), ('Hybrid', 'Hybrid'), ('Petrol', 'Petrol'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Automatic', 'Automatic'), ('Mannual', 'Mannual')], max_length=100),
        ),
    ]