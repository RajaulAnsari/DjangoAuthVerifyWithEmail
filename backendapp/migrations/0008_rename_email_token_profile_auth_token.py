# Generated by Django 5.0.1 on 2024-01-28 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0007_rename_user_profile_delete_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_token',
            new_name='auth_token',
        ),
    ]
