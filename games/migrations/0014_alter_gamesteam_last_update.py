# Generated by Django 4.2.14 on 2024-08-22 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_alter_gamesteam_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesteam',
            name='last_update',
            field=models.CharField(default=datetime.datetime(2024, 8, 22, 18, 14, 39, 258867, tzinfo=datetime.timezone.utc)),
        ),
    ]
