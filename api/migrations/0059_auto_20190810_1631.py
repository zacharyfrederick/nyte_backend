# Generated by Django 2.2.3 on 2019-08-10 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0058_auto_20190810_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionpairing',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.MenuOption'),
        ),
    ]