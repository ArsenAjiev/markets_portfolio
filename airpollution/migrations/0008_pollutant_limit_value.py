# Generated by Django 4.0.4 on 2022-05-02 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0007_alter_pollutantentry_pollution_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutant',
            name='limit_value',
            field=models.SmallIntegerField(null=True),
        ),
    ]
