# Generated by Django 3.0.4 on 2020-03-05 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200305_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='achievement',
            field=models.PositiveIntegerField(default=0, help_text='How much/many times do you do your habit?'),
        ),
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]