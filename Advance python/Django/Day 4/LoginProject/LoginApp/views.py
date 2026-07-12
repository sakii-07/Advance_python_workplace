from django.shortcuts import render
from .models import UserInfo

# Create your views here.

def getsigninpage(request):
    return render(request, 'signin.html')

def signin(request):
    username = request.GET['uname']
    passwd = request.GET['password']
    mob = request.GET['mobile']

    UserInfo.objects.create(
        uname = username,
        password = passwd,
        mobile = mob
    )

    return render(request, 'signIn.html',{'msg':'User created successfully ... '})