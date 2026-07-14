from django.shortcuts import render, redirect
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

    return render(request, 'signin.html',{'msg':'User Created successfully ...'})

def getupdatepage(request):
    return render(request, 'update.html')

def showuser(request):
    uname = request.GET['uname']

    if uname:
        userdb = UserInfo.objects.get(uname=uname)
        return render(request, 'update.html',{'userdb':userdb})
    else:
        return render(request, 'update.html', {'msg':'Invalid Username'})
    
def showall(request):
    userdb = UserInfo.objects.all()
    return render(request,'showall.html',{'userdb':userdb})
    
def update(request):
    uname = request.GET['uname']

    if uname:
        userdb = UserInfo.objects.filter(uname= uname)
        userdb.update(
            password = request.GET['password'],
            mobile = request.GET['mobile']
        )
        return redirect('showall')
    else:
        return render(request,'update.html',{'msg':'Invalid User..'})
    
def getdeletepage(request):
    return render(request, 'delete.html')

def showUserForDelete(request):
    uname = request.GET['uname']

    if uname:
        userdb = UserInfo.objects.get(uname = uname)
        return render(request, 'delete.html', {'userdb':userdb})
    else:
        return render(request,'delete.html', {'msg' : 'Invalid User'})
    
def delete(request):
    uname = request.GET['uname']

    if uname:
        UserInfo.objects.get(uname = uname).delete()
        return redirect('showall')
    else:
        return render(request,'delete.html', {'msg' : 'Invalid User'})
