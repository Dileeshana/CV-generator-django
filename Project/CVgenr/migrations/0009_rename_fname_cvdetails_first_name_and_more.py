# Generated by Django 4.0.4 on 2022-05-20 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenr', '0008_rename_name_cvdetails_fname_cvdetails_lname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvdetails',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='cvdetails',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='cvdetails',
            old_name='body',
            new_name='your_title',
        ),
        migrations.AddField(
            model_name='cvdetails',
            name='skill',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
