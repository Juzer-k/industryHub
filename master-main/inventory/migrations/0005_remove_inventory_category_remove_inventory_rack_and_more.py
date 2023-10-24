# Generated by Django 4.1.5 on 2023-02-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_inventory_category_inventory_rack_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='rack',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='warehouses',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='box_number',
        ),
        migrations.AddField(
            model_name='warehouse',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='state',
            field=models.CharField(choices=[('KA', 'Karnataka'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Kerala', 'Kerala'), ('Tamil Nadu', 'Tamil Nadu'), ('Maharashtra', 'Maharashtra'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Rajasthan', 'Rajasthan'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Telangana', 'Telangana'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Haryana', 'Haryana'), ('Jharkhand', 'Jharkhand'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Delhi', 'Delhi'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Lakshadweep', 'Lakshadweep'), ('Ladakh', 'Ladakh'), ('Puducherry', 'Puducherry')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
