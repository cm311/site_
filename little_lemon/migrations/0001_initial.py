# Generated by Django 4.1.7 on 2023-03-23 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_number', models.IntegerField()),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DrinkCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('shift', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('menu_item_description', models.TextField(default=' ', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftLogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('time_log', models.TimeField(help_text='Enter the exact time!')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=200)),
                ('prince', models.IntegerField()),
                ('category_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='little_lemon.drinkcategory')),
            ],
        ),
    ]
