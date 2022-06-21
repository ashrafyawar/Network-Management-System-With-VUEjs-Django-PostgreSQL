# Generated by Django 4.0.3 on 2022-05-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('AdminId', models.AutoField(primary_key=True, serialize=False)),
                ('AdminName', models.CharField(max_length=100)),
                ('AdminPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DemoRequest',
            fields=[
                ('DemoId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=10000)),
                ('Email', models.CharField(max_length=10000)),
                ('Message', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('DeviceId', models.AutoField(primary_key=True, serialize=False)),
                ('DeviceName', models.CharField(max_length=100)),
                ('DeviceIP', models.CharField(max_length=100)),
                ('DeviceModel', models.CharField(max_length=100)),
                ('DeviceStatus', models.BooleanField()),
                ('DeviceRecentLog', models.CharField(max_length=100)),
            ],
        ),
    ]
