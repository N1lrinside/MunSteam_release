# Generated by Django 4.2.14 on 2024-09-11 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0099_alter_gamesteam_last_update_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_news',
            field=models.DateField(default=datetime.datetime(2024, 9, 11, 18, 56, 29, 717474)),
        ),
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update_players',
            field=models.CharField(default=datetime.datetime(2024, 9, 11, 15, 56, 29, 717382, tzinfo=datetime.timezone.utc)),
        ),
    ]
