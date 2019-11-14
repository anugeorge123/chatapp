from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import View
from .forms import Signupform
from .models import User
import json

class Home(View):

    def get(self, request):
        signup_form = Signupform()
        return render(request,"index.html",{'signup':signup_form})

    def post(self,request):
        signup_dict={}
        signup_form = Signupform(request.POST)
        if signup_form.is_valid():
            print(self.request.POST)
            name = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            pwd = signup_form.cleaned_data['pwd']
            cpwd = signup_form.cleaned_data['cpwd']
            obj = User.objects.create_user(is_superuser="0", username=name, email=email, password=pwd)
            signup_dict['val']="success"
        else:
            signup_dict['val']= "failed"
        return HttpResponse(json.dumps(signup_dict), content_type="application/json")
