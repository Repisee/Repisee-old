# Generated by Django 3.1 on 2021-01-25 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
