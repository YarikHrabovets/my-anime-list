# Generated by Django 5.0.4 on 2024-05-16 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_anilistuser_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Anilist Profile', 'verbose_name_plural': 'Anilist Profiles'},
        ),
    ]