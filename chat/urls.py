from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^login/$', views.Login.as_view(), name="login"),
   url(r'^userProfile/$', views.UserProfile.as_view(), name="userProfile"),
   url(r'^chat/$', views.Chat.as_view(), name="chat"),
   # url(r'^<str:room_name>/$', views.Room.as_view(), name='room'),
   url(r'^chat/(?P<room_name>[\w.@+-]+)/$', views.Room.room, name="room"),
   url(r'^$', views.Home.as_view(), name="home"),
   ]
