# Generated by Django 2.1.7 on 2019-06-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190607_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='verification',
            name='image_data',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
