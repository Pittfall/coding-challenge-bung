# Generated by Django 2.1.7 on 2019-02-27 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_api', '0005_auto_20190226_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='last_sold_date',
        ),
        migrations.RemoveField(
            model_name='house',
            name='rentzestimate_last_updated',
        ),
        migrations.RemoveField(
            model_name='house',
            name='zestimate_last_updated',
        ),
    ]