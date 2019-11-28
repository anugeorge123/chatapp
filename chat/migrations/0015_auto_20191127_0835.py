# Generated by Django 2.2.7 on 2019-11-27 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20191126_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relfollower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='reluser', to=settings.AUTH_USER_MODEL),
        ),
    ]