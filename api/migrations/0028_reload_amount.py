# Generated by Django 2.1.7 on 2019-06-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_remove_reload_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reload',
            name='amount',
            field=models.FloatField(null=True),
        ),
    ]
