# Generated by Django 3.0.4 on 2020-03-06 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200305_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observer',
            old_name='user',
            new_name='observer',
        ),
    ]
