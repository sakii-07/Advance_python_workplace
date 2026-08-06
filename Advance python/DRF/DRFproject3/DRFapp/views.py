from django.shortcuts import render
from .models import LaptopInfo
from .serialization import LaptopInfoSeri
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def AddLaptop(request):
    serializer = LaptopInfoSeri(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def GetLaptop(request, laptop_id):
    laptop = LaptopInfo.objects.get(laptop_id = laptop_id)
    serializer = LaptopInfoSeri(laptop)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateLaptop(request,laptop_id):
    laptop = LaptopInfo.objects.get(laptop_id = laptop_id)
    serializer = LaptopInfoSeri(laptop, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def DeleteLaptop(request,laptop_id):
    LaptopInfo.objects.get(laptop_id = laptop_id).delete()
    return Response({'message':'Laptop Deleted successfully...'})

@api_view(['GET'])
def ShowAllLpatop(request):
    laptop_db = LaptopInfo.objects.all()
    serializer = LaptopInfoSeri(laptop_db, many = True)
    return Response(serializer.data)
