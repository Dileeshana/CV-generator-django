# Generated by Django 4.0.4 on 2022-05-21 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenr', '0012_remove_cvdetails_al_stream_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvdetails',
            name='avatar',
        ),
    ]
