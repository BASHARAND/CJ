# Generated by Django 2.2.7 on 2019-11-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageclass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='has',
            old_name='name',
            new_name='day',
        ),
        migrations.AddField(
            model_name='has',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]