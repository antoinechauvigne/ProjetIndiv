# Generated by Django 3.2.3 on 2021-05-17 20:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0002_post_priorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titre',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
