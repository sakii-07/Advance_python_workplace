from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentInfo
from .serializer import StudentInfoSeri

# Create your views here.

@api_view(['POST'])
def AddStudent(request):
    serializer = StudentInfoSeri(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET'])
def GetStudent(request,rollno):
    std_db = StudentInfo.objects.get(rollno = rollno)
    std_seri = StudentInfoSeri(std_db)
    return Response(std_seri.data)

@api_view(['PUT'])
def UpdateStudent(request, rollno):
    std_db = StudentInfo.objects.get(rollno = rollno)
    serializer = StudentInfoSeri(std_db, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def DeleteStudent(request,rollno):
    StudentInfo.objects.get(rollno = rollno).delete()
    return Response({"Message":'Student deleted successfully'})

