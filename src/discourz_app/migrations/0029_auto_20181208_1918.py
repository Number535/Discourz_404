# Generated by Django 2.1.1 on 2018-12-09 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discourz_app', '0028_auto_20181208_1907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='username',
            new_name='user',
        ),
    ]
