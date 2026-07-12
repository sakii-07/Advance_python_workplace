from django.shortcuts import render
from .models import UserInfo

# Create your views here.
def getsigninpage(request):
    return render(request, 'signin.html')

def signin(request):
    uname = request.GET['uname']
    password = request.GET['password']
    mobile = request.GET['mobile']

    UserInfo.objects.create(
        uname = uname,
        password = password,
        mobile = mobile
    )

    return render(request, 'signin.html', {'msg':'User created successfully ...'})