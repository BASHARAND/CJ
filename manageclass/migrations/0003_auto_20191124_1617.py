# Generated by Django 2.2.7 on 2019-11-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageclass', '0002_auto_20191124_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='has',
            name='time',
        ),
        migrations.AddField(
            model_name='has',
            name='a',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='b',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='c',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='d',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='e',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='f',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='g',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='h',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='l',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='m',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='n',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='has',
            name='w',
            field=models.IntegerField(default=0),
        ),
    ]
