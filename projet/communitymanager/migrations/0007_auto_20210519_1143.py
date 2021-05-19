# Generated by Django 3.2.3 on 2021-05-19 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0006_alter_commentaire_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='date_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_creation',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
