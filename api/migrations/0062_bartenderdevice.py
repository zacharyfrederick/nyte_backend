# Generated by Django 2.2.3 on 2019-08-12 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcm_django', '0004_auto_20181128_1642'),
        ('api', '0061_auto_20190812_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='BartenderDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcm_django.FCMDevice')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Venue')),
            ],
        ),
    ]
