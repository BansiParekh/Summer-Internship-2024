from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        # uname=request.POST.get('username')
        # password1 =request.POST.get('passsord1')
        # password2 =request.POST.get('passsord2')
        # my_user = User.objects.create_user(uname,password1)
        # my_user.save()
        # print(uname,password1,password2)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"User has been create Successfully")
            login(request,user)
            return redirect('chatbot')
    else:
        initial_data ={'username':'','password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"You have been Login Successfully")
            return redirect('chatbot')
    else:
        initial_data ={'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})

def dashboard_view(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def chatbot_view(request):
    return render(request,'chatbot.html')