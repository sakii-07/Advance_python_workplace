from django.shortcuts import render
from .models import Product
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

@api_view(['PUT'])
def UpdateProduct(request,product_id):
    product_db = Product.objects.get(product_id = product_id)
    serializer = ProductSeri(product_db, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def ShowAllProducts(request):
    product_db = Product.objects.all()
    serializer = ProductSeri(product_db,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetProduct(request,product_id):
    product_db = Product.objects.get(product_id=product_id)
    serializer = ProductSeri(product_db)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteProduct(request,product_id):
    Product.objects.get(product_id = product_id).delete()
    return Response({'msg':'Product deleted successfully...'})