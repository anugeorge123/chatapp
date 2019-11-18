from django import forms
from .models import User

class SignupForm(forms.Form):
    name = forms.CharField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Name'}))
    email = forms.EmailField(label='', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Your E-mail'}))
    pwd = forms.CharField(label='', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    cpwd = forms.CharField(label='', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))

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
        emails = User.objects.filter(email=email)

        for i in emails:
            if(i.email == email):
              raise forms.ValidationError("Email Already Exist!")
            if '@' in email:
              pass
            else:
                raise forms.ValidationError("Invalid Email")
        return email


class LoginForm(forms.Form):
    uname = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), label='')

    class Meta:
        model = User
