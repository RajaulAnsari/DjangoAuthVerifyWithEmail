# Generated by Django 5.0.1 on 2024-01-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0002_rename_firstname_userdata_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email_confirmation_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
