# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address =  models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = "User"


