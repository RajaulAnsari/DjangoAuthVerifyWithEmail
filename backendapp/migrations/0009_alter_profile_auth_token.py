# Generated by Django 5.0.1 on 2024-01-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0008_rename_email_token_profile_auth_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auth_token',
            field=models.CharField(max_length=100),
        ),
    ]
