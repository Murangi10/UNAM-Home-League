# Generated by Django 2.2.4 on 2019-11-12 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20191112_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixtures',
            name='Date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='Time',
            field=models.CharField(max_length=200),
        ),
    ]
