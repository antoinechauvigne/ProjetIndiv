# Generated by Django 3.2.3 on 2021-05-25 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0010_alter_post_date_evenement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_creation']},
        ),
    ]