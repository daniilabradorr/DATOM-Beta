# Generated by Django 5.0.6 on 2025-03-23 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_proyecto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='id_proyecto',
        ),
    ]
