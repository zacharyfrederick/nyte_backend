# Generated by Django 2.1.7 on 2019-05-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190507_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtoMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProtoOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=20)),
                ('status', models.CharField(default='ordered', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='nyteuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
