# Generated by Django 3.2.4 on 2021-06-22 17:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_rename_polluser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Polluser',
        ),
    ]
