# Generated by Django 5.0.6 on 2025-03-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proyecto', models.BigIntegerField()),
                ('nombre_proyecto', models.CharField(max_length=100)),
            ],
        ),
    ]
