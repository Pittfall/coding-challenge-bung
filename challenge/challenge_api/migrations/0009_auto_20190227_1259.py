# Generated by Django 2.1.7 on 2019-02-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_api', '0008_auto_20190227_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='home_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
