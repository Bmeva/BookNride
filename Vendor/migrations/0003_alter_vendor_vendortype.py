# Generated by Django 5.0.6 on 2024-06-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_vendor_vendortype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendorType',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Business', 'Business')], default='Individual', max_length=50),
        ),
    ]