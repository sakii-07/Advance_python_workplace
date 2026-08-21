from django.shortcuts import render
from .models import Product_info
from .serializer import ProductSeri
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def AddProduct(request):
    serializer = ProductSeri(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def GetProduct(requset, product_id):
    product_db = Product_info.objects.get(product_id=product_id)
    serializer = ProductSeri(product_db)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateProduct(request, product_id):
    product_id = Product_info.object.get(product_id=product_id)
    serializer = ProductSeri(product_id, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)   
