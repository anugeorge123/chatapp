from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View
from .forms import SignupForm, LoginForm
from .models import User, RoomName , Message, Following
from django.contrib.auth import login, authenticate, logout
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password


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
                # return HttpResponse(json.dumps(signup_dict), content_type="application/json")
            else:
                signup_dict['val']="failed"

                print("===========================>", signup_dict)
            return HttpResponse(json.dumps(signup_dict), content_type="application/json")
        else:
            signup_dict['val']= "failed"
            signup_dict['error']=signup_dict.errors
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
        query_contact = User.objects.all()
        return render(request,"chat/index.html",{'contact':query_contact})

    def post(self,request):
        list_name=[]
        print("post view ------------->")
        room_dict={}
        print("post method ------------->")
        room = request.POST['txt_room']

        username = self.request.user.username
        print(room)
        query_name = RoomName.objects.all()
        for i in query_name:
            list_name.append(i.name)
            print("room names",list_name)
        if room:
            if room not in list_name:
                print("inside if")
                query_room = RoomName(name=room,username=username)
                query_room.save()
                room_dict['val']="success"
                return HttpResponse(json.dumps(room_dict), content_type="application/json")
        else:
            room_dict['val'] = "failed"
        return HttpResponse(json.dumps(room_dict), content_type="application/json")
        # else:
        #     room_dict['val'] = "already exist"
        #     return HttpResponse(json.dumps(room_dict), content_type="application/json")


class Room(View):
    print("room view")
    def get(self,request, room_name):
        username = self.request.user.username
        obj = RoomName.objects.get(name=room_name)
        query_chat = Message.objects.filter(room=obj)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name)),'username': username,'room_name':room_name,'chat':query_chat
        })

    def post(self,request, room_name):
        msg_dict = {}
        print("inside room post")
        msg = request.POST['txt_msg']
        user = request.POST['user']
        current_user = self.request.user.username
        query_room = RoomName.objects.get(name=room_name)
        if current_user and msg:
            query_sent = Message(room=query_room,message = msg)
            query_sent.save()
            msg_dict["val"] = "success"
            return HttpResponse(json.dumps(msg_dict), content_type="application/json")
        else :
            msg_dict["val"]="failed"

        return HttpResponse(json.dumps(msg_dict), content_type="application/json")

# class Logout(View):
#     def get(self,request):
#         logout(request)
#         return render(request,"index.html")

class Followers(View):
    def get(self,request):
        return render(request,"followers.html")


class EditProfile(View):
    def get(self,request):
        user = self.request.user.username
        query_profile =User.objects.get(username=user)
        return render(request,"edit_profile.html",{'userDetails':query_profile})

    def post(self,request):
        profile_dict={}
        print("----------------",self.request.POST)
        user = self.request.user.username
        name=request.POST['txt_name']
        email = request.POST['txt_email']
        pwd = request.POST['txt_pwd']
        npwd = request.POST['txt_npwd']
        img =  request.FILES.get('img')
        print("-------->",img)
        query_user = User.objects.get(username=user)

        query_user.username = name
        query_user.email = email
        query_user.password = make_password(npwd)
        query_user.image = img
        print("passsssssssssssssssssssss",query_user.password)

        if name:
            query_user.save()
            profile_dict['val']="success"
        else:
            profile_dict['val']="Invalid Password Field"
        return HttpResponse(json.dumps(profile_dict), content_type="application/json")


class FollowingView(View):
    def get(self, request):
        query_user = User.objects.all().exclude(id=request.user.id)
        return render(request, "followinglist.html",{'userdeatils':query_user})

    def post(self, request):
        following_dict={}
        print("postttttttttttt",request.POST)
        user = request.POST['txt_userid']
        query_getuser = User.objects.get(id=user)
        print(query_getuser.username)
        name = query_getuser.username
        print(user)
        follower = self.request.user.username
        print(follower)
        try:
            query_all = Following.objects.all()
            for i in query_all:
                uname = i.follower
                query_following = Following.objects.get(follower=uname)
                if query_following:
                    query_following.user.add(query_getuser)
                    following_dict['val'] = "success"
                else:
                    query_following = Following.objects.create(follower=follower)
                    query_following.user.add(query_getuser)
                    following_dict['val'] = "success"

        except Exception as e:
            following_dict['val'] = "failed"
            print(e)
        return HttpResponse(json.dumps(following_dict), content_type="application/json")
