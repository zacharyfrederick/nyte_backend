# Generated by Django 2.2.3 on 2019-07-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20190630_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
