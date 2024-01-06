# Generated by Django 4.1 on 2023-12-16 15:44

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('systemapp', '0001_initial'), ('systemapp', '0002_second_second_systemapp_s_fname_019e1a_idx')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('date', django.contrib.postgres.fields.ranges.DateRangeField(default=['2023-01-01', '2023-01-03'])),
            ],
        ),
        migrations.AddIndex(
            model_name='first',
            index=models.Index(fields=['fname', 'date'], name='systemapp_f_fname_19f4bd_idx'),
        ),
        migrations.CreateModel(
            name='Second',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddIndex(
            model_name='second',
            index=models.Index(fields=['fname'], name='systemapp_s_fname_019e1a_idx'),
        ),
    ]
