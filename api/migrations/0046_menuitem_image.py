# Generated by Django 2.1.7 on 2019-07-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_transaction_is_data_formatted'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]