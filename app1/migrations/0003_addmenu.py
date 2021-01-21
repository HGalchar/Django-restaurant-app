# Generated by Django 3.0.7 on 2020-10-16 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201013_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='addMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish_name', models.CharField(max_length=100)),
                ('Dish_type', models.CharField(max_length=50)),
                ('Dish_price', models.CharField(max_length=20)),
                ('R_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.addRestaurants')),
            ],
        ),
    ]