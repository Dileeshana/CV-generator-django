# Generated by Django 4.0.4 on 2022-05-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenr', '0011_remove_cvdetails_skill_cvdetails_skill1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvdetails',
            name='al_stream',
        ),
        migrations.RemoveField(
            model_name='cvdetails',
            name='ol_result',
        ),
        migrations.AddField(
            model_name='cvdetails',
            name='education',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cvdetails',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cvdetails',
            name='experience',
            field=models.TextField(null=True),
        ),
    ]
