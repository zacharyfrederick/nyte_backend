# Generated by Django 2.1.7 on 2019-05-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nyteuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
