# Generated by Django 4.2.13 on 2024-06-21 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('requirements', models.CharField(max_length=1000)),
                ('resources', models.CharField(max_length=500)),
            ],
        ),
    ]
