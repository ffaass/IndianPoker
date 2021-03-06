# Generated by Django 3.1.1 on 2020-10-06 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('73f4b189-0159-4c0d-b313-9c32c99cbdcd'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('group_name', models.SlugField(unique=True)),
                ('state', models.IntegerField(default=0)),
                ('round', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('ready_state', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=10)),
            ],
        ),
    ]
