# Generated by Django 4.1.5 on 2023-01-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_category_warehouse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Wa',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rack',
            name='description',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]