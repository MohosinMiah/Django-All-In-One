# Generated by Django 2.2.4 on 2019-08-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='favorite',
        ),
        migrations.AddField(
            model_name='song',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
