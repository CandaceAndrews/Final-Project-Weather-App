# Generated by Django 4.2 on 2023-04-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0003_rename_temperature_weather_temp_remove_weather_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='temp',
        ),
        migrations.AddField(
            model_name='weather',
            name='weather_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
