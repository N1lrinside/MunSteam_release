# Generated by Django 4.2.14 on 2024-08-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_gameachievement_app_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameuser',
            name='user',
        ),
        migrations.AddField(
            model_name='gameuser',
            name='user_steam_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]