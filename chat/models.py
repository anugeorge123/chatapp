# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    followers = models.IntegerField(null=True, blank=True,default=0)
    following = models.IntegerField(null=True, blank=True,default=0)
    messages = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    class Meta:
        db_table = "user"
        verbose_name_plural = "User"


class RoomName(models.Model):
    name = models.TextField(max_length=100,null=True,blank=True)
    username =models.TextField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = "roomname"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(RoomName,on_delete=models.CASCADE, related_name='messages',null=True)
    user = models.CharField(max_length=100,null=True, blank=True)
    message = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.message

class Following(models.Model):
    following = models.ManyToManyField(User, blank=True, related_name='reluser')
    follower = models.ForeignKey(User,on_delete=models.CASCADE, related_name='relfollower',null=True)

    class Meta:
        db_table = "following"

    def __str__(self):
        return self.follower.username




