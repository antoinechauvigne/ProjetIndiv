# Generated by Django 3.2.3 on 2021-05-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0011_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]
