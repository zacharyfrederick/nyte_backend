# Generated by Django 2.1.7 on 2019-06-28 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20190628_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='reload',
            name='stripe_transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
