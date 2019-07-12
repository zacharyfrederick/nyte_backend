# Generated by Django 2.2.3 on 2019-07-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_menuitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tip',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='convenience_fee',
            field=models.FloatField(blank=True, default=-1.0, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
