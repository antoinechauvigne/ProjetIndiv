# Generated by Django 3.2.3 on 2021-05-19 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0007_auto_20210519_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
