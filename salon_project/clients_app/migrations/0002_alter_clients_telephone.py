# Generated by Django 4.2.17 on 2025-01-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='telephone',
            field=models.CharField(max_length=12),
        ),
    ]