# Generated by Django 2.1.7 on 2019-06-30 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20190630_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='NyteVenue',
            new_name='venue',
        ),
    ]