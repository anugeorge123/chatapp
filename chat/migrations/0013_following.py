# Generated by Django 2.2.7 on 2019-11-26 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_auto_20191125_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('user', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'following',
            },
        ),
    ]
