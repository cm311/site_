# Generated by Django 4.1.7 on 2023-03-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_site_main', '0002_wh3lord'),
    ]

    operations = [
        migrations.AddField(
            model_name='wh3lord',
            name='icon',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
