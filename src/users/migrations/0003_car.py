# Generated by Django 4.1.3 on 2022-11-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_website_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
