# Generated by Django 3.0.7 on 2020-10-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addRestaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_name', models.CharField(max_length=100)),
                ('R_ownername', models.CharField(max_length=100)),
                ('R_mobileno', models.IntegerField()),
                ('R_adress', models.CharField(max_length=100)),
                ('R_type', models.CharField(max_length=20)),
            ],
        ),
    ]
