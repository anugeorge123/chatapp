# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.IntegerField(null=True, blank=True,default=0)
    following = models.IntegerField(null=True, blank=True,default=0)
    messages = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = "User"


