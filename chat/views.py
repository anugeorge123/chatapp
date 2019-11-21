from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View
from .forms import SignupForm, LoginForm
from .models import User, RoomName , Message
from django.contrib.auth import login, authenticate, logout
import json
from django.utils.safestring import mark_safe

class Home(View):

    def get(self, request):
        signup_form = SignupForm()
        return render(request,"index.html",{'signup':signup_form})

    def post(self,request):
        signup_dict={}
        signup_form = SignupForm(request.POST)
        print(signup_form.errors)
        if signup_form.is_valid():
            print(self.request.POST)
            name = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            pwd = signup_form.cleaned_data['pwd']
            cpwd = signup_form.cleaned_data['cpwd']
            print(name,email,pwd,cpwd)
            if(pwd==cpwd):
                obj = User.objects.create_user(is_superuser="0", username=name, email=email, password=pwd)
                obj.save()
                signup_dict['val']="success"
                return HttpResponse(json.dumps(signup_dict), content_type="application/json")
            else:
                signup_form['val']="failed"
        else:
            signup_dict['val']= "failed"
        return HttpResponse(json.dumps(signup_dict), content_type="application/json")

class Login(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, "login1.html", {'login': login_form})

    def post(self, request):

        log_dict = {}
        login_form = LoginForm(request.POST)
        print(login_form.errors)
        if login_form.is_valid():
            uname = login_form.cleaned_data['uname']
            pwd = login_form.cleaned_data['pwd']
            print("uname: ", uname, "password: ", pwd)
            try:
                obj = User.objects.get(username=uname)
                auth1 = authenticate(request, username=uname, password=pwd)
                print(auth1)
                if auth1:
                    login(request, auth1, backend='django.contrib.auth.backends.ModelBackend')
                    log_dict['val'] = "success"
                    return HttpResponse(json.dumps(log_dict), content_type="application/json")
                else:
                    log_dict['val'] = "failed"
                    return HttpResponse(json.dumps(log_dict), content_type="application/json")
            except Exception as e:
                print(e)


class UserProfile(View):

	def get(self,request):
		login_user = request.user
		query_user = User.objects.get(username=login_user)
		return render(request,"user_profile.html",{'user':query_user})


class Chat(View):
    print("chat view ------------->")
    def get(self,request):
        print("get view ------------->")
        return render(request,"chat/index.html")

    def post(self,request):
        print("post view ------------->")
        room_dict={}
        print("post method ------------->")
        room = request.POST['txt_room']
        username = self.request.user.username
        print(room)
        if room:
            print("inside if")
            query_room = RoomName(name=room,username=username)
            query_room.save()
            room_dict['val']="success"
        else:
            room_dict['val'] = "failed"
        # return render(request, "chat/room.html")
        return HttpResponse(json.dumps(room_dict), content_type="application/json")

class Room(View):
    def get(self,request, room_name):
        print("******")
        username = self.request.user.username
        print(room_name)
        obj = RoomName.objects.get(name=room_name)
        print("obj",obj)
        query_chat = Message.objects.filter(room=obj)
        print("query chat==",query_chat)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),'username': username,'room_name':room_name,'chat':query_chat
        })

    def post(self,request, room_name):
        msg_dict = {}
        print("inside room post")
        msg = request.POST['txt_msg']
        username = self.request.user.username
        print(username, "---",room_name)
        query_room = RoomName.objects.get(name=room_name)
        print(query_room.name)
        if username and msg:
            print("inside if")
            query_sent = Message(room=query_room,message = msg)
            query_sent.save()
            msg_dict["val"] = "success"
        else :
            msg_dict["val"]="failed"
        return HttpResponse(json.dumps(msg_dict), content_type="application/json")

