from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect 
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.views.generic import View
from managementapp.models import Contact
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import idna

from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage

from django.contrib.auth.tokens import PasswordResetTokenGenerator

def index(request): 
	return render(request, 'index.html') 


def contact(request): 

	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		desc = request.POST.get("desc")
		phonenumber = request.POST.get("phonenumber")
		myquery = Contact(name=name, email=email, desc=desc,
					phonenumber=phonenumber)
		myquery.save()
	messages.info(request, "we'll get back to you soon..")
	

	return render(request, 'contact.html') 


def signup(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password1']
		confirmpass=request.POST['pass2']
		if password!=confirmpass:
			messages.warning("password dint match")
			return render(request,'signup.html')
		try:
			if User.objects.get(username=email):
				messages.info("email already exists!")
				return render (request,'signup.html')
			
		except Exception as identifier: 
			pass
		user=User.objects.create_user(email,email,password)
		user.save()
		
	return render(request,'signup.html')

def login(request): 
	
	if request.POST:
		username=request.POST['email']
		userpassword=request.POST['pass1']
		myuser=authenticate(username=username,password=userpassword)
		if myuser is not None:
			login(request,myuser)
			messages.success(request,"login succesfull")
			return render(request,'home.html')
		else:
			messages.error(request,'invalid credentials')
			return render(request,'login')

		
	return render(request, 'login.html') 



def logout(request):
	logout(request)
	messages.info(request,"logout successful")
	
	
	return render(request,'login.html')

def news(request):
	





	return render(request,'news.html')

def about(request):
	return render(request,'about.html')