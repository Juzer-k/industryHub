# Generated by Django 4.1.5 on 2023-01-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_category_wa_category_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='rack',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouses',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
