# Generated by Django 2.2.3 on 2019-08-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0062_bartenderdevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
