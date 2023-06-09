# Generated by Django 4.2 on 2023-04-28 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('is_it_raining', '0029_remove_capturedanimal_captured_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='team-fries-images')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_animal', to='is_it_raining.animal')),
            ],
        ),
        migrations.CreateModel(
            name='CapturedSpecialAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_owner', to=settings.AUTH_USER_MODEL)),
                ('special_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_animal', to='is_it_raining.specialanimal')),
            ],
        ),
    ]
