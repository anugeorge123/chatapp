# Generated by Django 2.2.7 on 2019-11-27 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20191127_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='following',
            old_name='user',
            new_name='following',
        ),
    ]
