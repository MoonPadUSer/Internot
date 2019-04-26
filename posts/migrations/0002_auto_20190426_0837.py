# Generated by Django 2.2 on 2019-04-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='parent_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='post',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
