"""from django import forms
from .models import register
import re
from django.contrib.auth import authenticate,login

#class registerForm(forms.Form):
	class Meta:
		model=register
		widgets = {
		'password' : forms.PasswordInput(attrs={
			'placeholder' : 'Password'
			}),
		'email' : forms.EmailInput(attrs={
			'placeholder' : 'Email'
			}),
		'name' : forms.TextInput(attrs={
			'placeholder' : 'Name'
			})
		}
		fields = ['name','email','password']

	def clean_email(self):
		email=self.cleaned_data['email']
		userid,domain=email.split("@")
		if bool(re.search(r'\d',domain)):
			raise forms.ValidationError("Enter a proper Email")
		else:
			return email

	def clean_name(self):
		name=self.cleaned_data['name']
		if len(name) < 3 :
			raise forms.ValidationError("Enter Your Full Name")
		elif bool(re.search(r'\d',name)):
			raise forms.ValidationError("Enter only character")
		else:
			return name

	def clean_password(self):
		password=self.cleaned_data['password']
		if len(password) < 6:
			raise forms.ValidationError("Enter Minimum 6 characters")
		else:
			return password
		#if bool(re.search(r'',password))

class loginForm(forms.Form):
	email=forms.EmailInput(attrs={
		'placeholder' : 'Email'
		})
	password=forms.PasswordInput(attrs={
		'placeholder' : 'Password'
		})
	def clean(self):
		email=self.cleaned_data['email']
		password=self.cleaned_data['password']
		user = authenticate(username=email,password=password)
		if not user or user.is_active:
			raise forms.ValidationError("othaa thirutu koothi")
		else:
			return self.cleaned_data

	def login(self,request):
		email=self.cleaned_data['email']
		password=self.cleaned_data['password']
		user = authenticate(username=email,password=password)
		return user"""	
from django import forms

class registerForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )