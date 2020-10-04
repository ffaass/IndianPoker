# Generated by Django 3.1.1 on 2020-09-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=10)),
                ('round', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('ready_state', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=10)),
            ],
        ),
    ]
