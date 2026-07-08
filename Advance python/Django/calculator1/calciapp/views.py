from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("Good morning")

def getadditionpage(request):
    return render(request,'addition.html')

def addition(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) + int(num2)

    return render(request,'addition.html', {'num1':num1,'num2':num2,'answer':answer})

def getsubpage(request):
    return render(request, 'sub.html')

def sub(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    answer = int(num1) - int(num2)
    return render(request, 'sub.html',{'num1':num1,'num2':num2,'answer':answer})

def getmulpage(request):
    return render(request, 'mul.html')

def mul(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    answer = int(num1) * int(num2)
    return render(request, 'mul.html',{'num1':num1,'num2':num2,'answer':answer})

def getdivpage(request):
    return render(request, 'div.html')

def div(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    answer = int(num1) / int(num2)
    return render(request, 'div.html',{'num1':num1,'num2':num2,'answer':answer})

def getfloordivpage(request):
    return render(request, 'floordiv.html')

def floordiv(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    answer = int(num1) // int(num2)
    return render(request, 'floordiv.html',{'num1':num1,'num2':num2,'answer':answer})
