# Generated by Django 2.2.3 on 2019-08-27 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0073_auto_20190827_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nyteuser',
            name='id_image',
            field=models.ImageField(default='None', null=True, upload_to=''),
        ),
    ]
