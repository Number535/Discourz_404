# Generated by Django 2.1.1 on 2018-12-01 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discourz_app', '0014_auto_20181130_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='polltopic',
            name='category',
            field=models.TextField(default='', max_length=100),
        ),
    ]