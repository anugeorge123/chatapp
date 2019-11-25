# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from .models import User,RoomName,Message

class UserAdmin(admin.ModelAdmin):
     list_display = ('username', 'email',)


admin.site.register(User, UserAdmin)
admin.site.register(RoomName, admin.ModelAdmin)
admin.site.register(Message,admin.ModelAdmin)