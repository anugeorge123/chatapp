from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^login/$', views.Login.as_view(), name="login"),
   url(r'^userProfile/$', views.UserProfile.as_view(), name="userProfile"),
   url(r'^chat/$', views.Chat.as_view(), name="chat"),
   # url(r'^<str:room_name>/$', views.Room.as_view(), name='room'),
   url(r'^chat/(?P<room_name>[\w.@+-]+)/$', views.Room.as_view(), name="room"),
   # url(r'^$', views.Logout.as_view(), name="logout"),
   url(r'^followers/$',views.Followers.as_view(), name="followers"),
   url(r'^editProfile/$',views.EditProfile.as_view(), name="editprofile"),
   url(r'^following/$',views.FollowingView.as_view(), name="mytemplate"),

   url(r'^$', views.Home.as_view(), name="home"),
   ]
