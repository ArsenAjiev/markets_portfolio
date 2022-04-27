# Generated by Django 4.0.4 on 2022-04-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0002_remove_pollutantentry_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AddField(
            model_name='country',
            name='iso_code',
            field=models.CharField(default='AA', max_length=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]