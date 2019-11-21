# Generated by Django 2.2.7 on 2019-11-20 09:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20191118_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('label', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.TextField()),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.Room')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]