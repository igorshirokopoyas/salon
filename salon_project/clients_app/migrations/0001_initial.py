# Generated by Django 4.2.17 on 2025-01-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=11)),
                ('last_visit_date', models.DateTimeField()),
            ],
        ),
    ]
