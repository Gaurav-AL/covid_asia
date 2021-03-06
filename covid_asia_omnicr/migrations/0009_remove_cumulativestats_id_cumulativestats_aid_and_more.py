# Generated by Django 4.0.2 on 2022-02-13 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_asia_omnicr', '0008_alter_deltastats_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cumulativestats',
            name='id',
        ),
        migrations.AddField(
            model_name='cumulativestats',
            name='aid',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deltastats',
            name='Latest_Confirmed',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deltastats',
            name='Latest_Deaths',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deltastats',
            name='Latest_Recovered',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cumulativestats',
            name='Confirmed',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cumulativestats',
            name='Country',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cumulativestats',
            name='Deaths',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cumulativestats',
            name='Recovered',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deltastats',
            name='Active',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deltastats',
            name='Country',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deltastats',
            name='Death',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deltastats',
            name='Recovered',
            field=models.CharField(default='NA', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deltastats',
            name='Time',
            field=models.TimeField(default=datetime.time(14, 30, 0, 298611)),
        ),
    ]
