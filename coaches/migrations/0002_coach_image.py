# Generated by Django 4.2.13 on 2024-07-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
