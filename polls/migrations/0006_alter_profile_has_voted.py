# Generated by Django 3.2.4 on 2021-06-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_polluser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
    ]
