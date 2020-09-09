# Generated by Django 3.0.7 on 2020-09-02 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorRegistrationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stall_name', models.CharField(max_length=200)),
                ('contact_1', models.IntegerField(unique=True)),
                ('contact_2', models.IntegerField(unique=True)),
                ('photo', models.ImageField(upload_to='vendor_images/')),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('OTP', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('cuisine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_admin.CuisineModel')),
                ('vendor_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_admin.CityModel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodTypeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=30)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.VendorRegistrationModel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItemsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='fooditems/')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.FoodTypeModel')),
            ],
        ),
    ]
