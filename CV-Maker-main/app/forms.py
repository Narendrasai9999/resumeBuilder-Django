from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class':'form-control my-2'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs = {'class':'form-control my-2'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs = {'class':'form-control my-2'}),
        'email':forms.EmailInput(attrs = {'class':'form-control my-2'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs = {'autofocus':True,'class':'form-control my-2'}))

    password = forms.CharField(label='Password',strip=False, widget=forms.PasswordInput(attrs = {'autocomplete': 'current-password','class':'form-control my-2'}))

