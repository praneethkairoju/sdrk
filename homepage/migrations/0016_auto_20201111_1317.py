# Generated by Django 3.1.2 on 2020-11-11 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0015_remove_service_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post',
        ),
        migrations.AddField(
            model_name='service',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
    ]