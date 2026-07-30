from django.shortcuts import render
from .serializer import UserInfoSeri
from .models import UserInfo
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def AddUser(request):
    serializer = UserInfoSeri(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def GetUser(request,username):
    userdb = UserInfo.objects.get(username = username)
    useri = UserInfoSeri(userdb)
    return Response(useri.data)

@api_view(['PUT'])
def UpdateUser(request, username):
    userdb = UserInfo.objects.get(username = username)
    serializer = UserInfoSeri(userdb, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def DeleteUser(request,username):
    UserInfo.objects.filter(username = username).delete()
    return Response({"msg":"User deleted successfully "})