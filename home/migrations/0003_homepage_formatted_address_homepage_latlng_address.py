# Generated by Django 4.1.13 on 2023-11-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='formatted_address',
            field=models.CharField(default='x', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='latlng_address',
            field=models.CharField(default='TEST', max_length=255),
            preserve_default=False,
        ),
    ]
