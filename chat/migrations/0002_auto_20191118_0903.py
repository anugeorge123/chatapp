# Generated by Django 2.2.7 on 2019-11-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='messages',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]