# Generated by Django 4.2 on 2023-04-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0014_rename_image_weathericon_icon_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]