# Generated by Django 2.2.4 on 2019-11-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
