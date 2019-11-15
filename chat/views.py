from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib.auth import login, authenticate, logout
import json

class Home(View):

    def get(self, request):
        signup_form = SignupForm()
        # login_form = LoginForm()
        return render(request,"index.html",{'signup':signup_form})

    def post(self,request):
        print("posttttttttttttttttttttttttttt")
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
        return render(request, "login.html", {'login': login_form})

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
