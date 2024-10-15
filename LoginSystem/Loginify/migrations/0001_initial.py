# Generated by Django 4.1 on 2024-10-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('Username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(blank=True, max_length=12)),
            ],
        ),
    ]
