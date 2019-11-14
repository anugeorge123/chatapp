from django import forms
from .models import User


class Signupform(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    cpwd = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_pwd(self):
        password = self.cleaned_data.get('pwd')
        if(password == ""):
            raise forms.ValidationError("This field is required!!")
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if(email == ""):
            raise forms.ValidationError("This field is required!!")
        emails = Realuser.objects.filter(email=email)

        for i in emails:
            if(i.email == email):
              raise forms.ValidationError("Email Already Exist!")
            if '@' in email:
              pass
            else:
                raise forms.ValidationError("Invalid Email")
        return email