# Generated by Django 4.0.2 on 2022-02-12 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_asia_omnicr', '0002_asia_date_asia_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asia',
            name='Time',
            field=models.TimeField(default=datetime.time(13, 38, 28, 602835)),
        ),
    ]