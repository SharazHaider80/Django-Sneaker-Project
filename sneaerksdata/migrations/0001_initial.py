# Generated by Django 3.2.7 on 2021-10-03 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=30)),
                ('product_url', models.URLField(default=None, null=True)),
                ('sku', models.CharField(max_length=30)),
                ('availability', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sneakers_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(default=None, max_length=30, null=True)),
                ('product_type', models.CharField(default=None, max_length=30, null=True)),
                ('low_price', models.IntegerField(default=None, null=True)),
                ('average_price', models.IntegerField(default=None, null=True)),
                ('highest_price', models.IntegerField(default=None, null=True)),
                ('brand_name', models.IntegerField(default=None, null=True)),
                ('color', models.CharField(default=None, max_length=30, null=True)),
                ('designer', models.CharField(default=None, max_length=30, null=True)),
                ('nick_name', models.CharField(default=None, max_length=30, null=True)),
                ('release_date', models.DateField(default=None, null=True)),
                ('release_year', models.IntegerField(default=None, null=True)),
                ('slug', models.TextField(default=None, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('material', models.TextField(default=None, null=True)),
                ('product_placeholder', models.TextField(default=None, null=True)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendorsId', to='sneaerksdata.vendors')),
            ],
        ),
    ]
