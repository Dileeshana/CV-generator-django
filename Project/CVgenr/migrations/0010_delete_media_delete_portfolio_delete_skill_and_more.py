# Generated by Django 4.0.4 on 2022-05-20 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenr', '0009_rename_fname_cvdetails_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.AddField(
            model_name='cvdetails',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
