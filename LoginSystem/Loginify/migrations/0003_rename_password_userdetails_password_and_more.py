# Generated by Django 4.1 on 2024-10-12 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loginify', '0002_rename_email_userdetails_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='Username',
            new_name='username',
        ),
    ]