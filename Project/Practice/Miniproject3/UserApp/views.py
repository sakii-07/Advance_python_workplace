from django.shortcuts import render
from .models import UserInformation

# Create your views here.
def GetCheckUserInfo(request):
    return render(request, 'checkuser.html')

def CheckUser(request):
    try:
        uid = request.GET['uid']

        user = UserInformation.objects.get(uid = uid)

        if user:
            return render(request, 'checkuser.html',{'msg':'User Exist with salary : ','user':user})
        else:
            return render(request, 'checkuser.html',{'msg':'User not Exist'})
    except Exception as e:
        return render(request, 'checkuser.html',{'msg':'User not Exist'})