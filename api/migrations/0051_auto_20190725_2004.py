# Generated by Django 2.2.3 on 2019-07-25 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20190724_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuoption',
            name='menu_item',
        ),
        migrations.AddField(
            model_name='menuoption',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AlterField(
            model_name='optionvalue',
            name='option',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.MenuOption'),
        ),
    ]
