# Generated by Django 2.2.3 on 2019-08-10 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_remove_optionvalue_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionvalue',
            name='option',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='values', to='api.MenuOption'),
        ),
    ]
