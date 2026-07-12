from django.shortcuts import render
from .models import SigninInfo

# Create your views here.

def getsignpage(request):
    return render(request, 'signin.html')

def signin(request):
    uname = request.GET['uname']
    password = request.GET['password']
    mobile = request.GET['mobile']

    SigninInfo.objects.create(
        uname = uname,
        password = password,
        mobile = mobile
    )

    return render(request, 'signin.html', {'msg': 'SignIn Successfully...'})
