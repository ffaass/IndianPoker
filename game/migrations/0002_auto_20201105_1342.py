# Generated by Django 3.1.1 on 2020-11-05 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]