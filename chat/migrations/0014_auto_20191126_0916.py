# Generated by Django 2.2.7 on 2019-11-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='follower',
            field=models.TextField(blank=True, null=True),
        ),
    ]
