from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            user=User.objects.create_user(first_name=username,username=username,email=email,password=password)

            print(username,email,password,confirmpassword)
            return render(request,'Account/login.html')
    return render(request,'Account/signup.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('homepage')
        else:
            return render(request,'User/login.html')
    return render(request,'Account/login.html')

def logout_view(request):
    logout(request)
    return redirect("/")