from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserRegistrationForm(UserCreationForm, forms.Form):
	fullname = forms.CharField(label='Full Name')
	state = forms.CharField(label='State')
	country = forms.CharField(label='Country')
	pincode = forms.CharField(label='Pincode')

	class Meta:
		model = User
		fields = ['fullname', 'email', 'password1', 'password2', 'state', 'country', 'pincode', 'gender']


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())