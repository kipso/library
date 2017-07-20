"""from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from .forms import registerForm,loginForm
def register(request):
	if request.method =='POST':
		form=registerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/signup/profile/')
	else:
		form=registerForm()

	args={'form' : form}
	return render (request,'register.html',args)

def profile(request):
	return render(request,'profile.html',{})

def log(request):
	form=loginForm(request.POST or None)
	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			login(request,user)
			return redirect('/signup/profile/')
	return render (request,'login.html',{'login_form' : form})"""

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import registerForm
from django.shortcuts import render_to_response
from .models import books
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/signup/profile/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = registerForm()

    return render(request, 'register.html', {'form' : form})

def profile(request):
	obj = books.objects.all()
	return render(request,'profile.html',{'obj' : obj})

def about(request):
	return render(request,'about.html',{})

def lend(request):
	a = books.objects.only('title')
	print(a)
	count = a
	a = count
	print(count)
	 #a.save()

	"""a = request.GET
	b= a.get(id=)
	print (b)
	#print (request)
	#print(title)"""		
	return redirect('/signup/profile/')


def returned(request):
	a = books.objects.only('title')
	print(a)
	count = a
	a = count
	print(count)		
	return redirect('/signup/profile/')	
#def display_book(request):
