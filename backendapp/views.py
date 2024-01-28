from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from backendapp.models import Profile
from .models import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


@login_required
def home(request):
    return render(request,'home.html')

def custom_login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        checkuser=User.objects.filter(email=email).first()
        print(password)
        if checkuser is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')
       
        
        profile_obj = Profile.objects.filter(user = checkuser ).first()
            
        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')
        
        
        user = authenticate(email= email , password = password)
        if user is None :
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        auth_login(request,user)
        return redirect('/')
        
        
    return render(request,'login.html')



def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(password)
        
        # if first_name and last_name and email and password: 
        try:
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/create')
            username = str(uuid.uuid4().int % (999999999 - 111111111 + 1) + 111111111)
            user_obj = User(first_name=first_name,last_name=last_name,email=email,username=username)
            user_obj.set_password(password)
            user_obj.save()
            auth_token=str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email,auth_token)
            return redirect('/token')
        except Exception as e:
            print(e)

    return render(request,'create.html')

    
def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')






def verify(request,auth_token):
    try:
        user=Profile.objects.filter(auth_token=auth_token).first()
        
        if user:
            if user.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            user.is_verified=True
            user.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return request('/')
    
    
def error_page(request):
    return  render(request , 'error.html')
    
    
def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    
    
    
def logout_view(request):

    return redirect(reverse('login'))  
 