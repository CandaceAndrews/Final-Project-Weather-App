# Generated by Django 4.2 on 2023-04-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0034_remove_background_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='music'),
        ),
    ]