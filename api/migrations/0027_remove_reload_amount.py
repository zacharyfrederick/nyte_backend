# Generated by Django 2.1.7 on 2019-06-28 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20190628_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reload',
            name='amount',
        ),
    ]