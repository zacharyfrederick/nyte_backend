# Generated by Django 2.2.3 on 2019-08-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_auto_20190814_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='notification_status',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]