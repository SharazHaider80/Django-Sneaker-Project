# Generated by Django 3.2.7 on 2021-10-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneaerksdata', '0006_auto_20211005_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakers_data',
            name='average_price',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sneakers_data',
            name='highest_price',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sneakers_data',
            name='low_price',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]