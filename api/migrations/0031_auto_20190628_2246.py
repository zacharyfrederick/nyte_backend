# Generated by Django 2.1.7 on 2019-06-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_reload_stripe_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reload',
            name='payment_source',
        ),
        migrations.AddField(
            model_name='reload',
            name='card',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
