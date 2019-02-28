# Generated by Django 2.1.7 on 2019-02-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(max_length=255)),
                ('bathrooms', models.FloatField()),
                ('bedrooms', models.IntegerField()),
                ('home_size', models.IntegerField()),
                ('home_type', models.CharField(max_length=100)),
                ('last_sold_date', models.DateField()),
                ('last_sold_price', models.IntegerField()),
                ('link', models.URLField()),
                ('price', models.FloatField()),
                ('property_size', models.IntegerField()),
                ('rent_price', models.IntegerField()),
                ('rent_estimation_amount', models.IntegerField()),
                ('rent_estimation_date', models.DateField()),
                ('tax_value', models.IntegerField()),
                ('tax_year', models.IntegerField()),
                ('year_build', models.IntegerField()),
                ('estimate_amount', models.IntegerField()),
                ('estimation_last_update', models.DateField()),
                ('zillow_id', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]
