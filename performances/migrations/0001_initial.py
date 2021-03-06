# Generated by Django 4.0.2 on 2022-04-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('revenue', models.FloatField()),
                ('profit', models.FloatField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HourlyPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('revenue', models.FloatField()),
                ('profit', models.FloatField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
