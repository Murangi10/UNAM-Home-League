# Generated by Django 2.2.4 on 2019-11-12 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20191112_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixtures',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='fixtures',
            name='Time',
        ),
    ]
