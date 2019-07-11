# Generated by Django 2.1.7 on 2019-06-29 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_transaction_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='order_total',
            new_name='total',
        ),
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='failure_code',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='failure_message',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='has_attempted_to_charge',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='transaction',
            name='stripe_transaction_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]