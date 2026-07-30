from django.shortcuts import render, redirect
from .models import UserInfo

# Create your views here.

def GetUserPage(request):
    return render(request, 'user.html')

def CheckUser(request):
    username = request.GET['username']

    uname = UserInfo.objects.filter(username=username).exists()

    if uname:
        return render(request,'user.html',{'msg':'Username Exist'})
    
    return render(request,'user.html',{'msg':'Username Not Exist','username':username})


def GetaddUserPage(request):
    return render(request, 'add_user.html')

def AddUser(request, username):
    if username:
        UserInfo.objects.create(
            username = username
        )
    return render(request, 'user.html',{'msg':'user added successfully'})



