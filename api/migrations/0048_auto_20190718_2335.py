# Generated by Django 2.2.3 on 2019-07-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20190712_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
