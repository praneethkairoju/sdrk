# Generated by Django 3.1.2 on 2020-11-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20201111_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]