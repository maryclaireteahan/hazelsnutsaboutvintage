# Generated by Django 3.2.23 on 2024-01-07 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20240107_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
    ]
