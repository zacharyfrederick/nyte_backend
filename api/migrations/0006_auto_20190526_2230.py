# Generated by Django 2.1.7 on 2019-05-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_protomenuitem_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protoorder',
            name='status',
            field=models.CharField(choices=[('or', 'Ordered'), ('ma', 'Making'), ('re', 'Ready'), ('pi', 'Picked up')], default='or', max_length=100),
        ),
    ]
