# Generated by Django 2.2.3 on 2019-07-24 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20190718_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('default', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('multiple_allowed', models.BooleanField(blank=True, default=False, null=True)),
                ('required', models.BooleanField(blank=True, default=False, null=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MenuItem')),
            ],
        ),
    ]