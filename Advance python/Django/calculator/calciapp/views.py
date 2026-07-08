from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greet(request):
    return HttpResponse("Good morning")

def getadditionpage(request):
    return render(request, 'addition.html')

def addition(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) + int(num2)

    return render(request, 'addition.html', {'num1':num1, 'num2':num2,'answer':answer})

def getsubstractionpage(request):
    return render(request, 'substraction.html')

def substraction(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) - int(num2)

    return render(request, 'substraction.html', {'num1':num1,'num2':num2,'answer':answer})

def getmultiplicationpage(request): 
    return render(request, 'multiplication.html')

def multiplication(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) * int(num2)
    return render(request, 'multiplication.html',{'num1':num1,'num2':num2,'answer':answer})

def getdivisionpage(request): 
    return render(request, 'division.html')

def division(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) / int(num2)
    return render(request, 'division.html',{'num1':num1,'num2':num2,'answer':answer})

def getfloordivisionpage(request): 
    return render(request, 'floordivision.html')

def floordivision(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) // int(num2)
    return render(request, 'floordivision.html',{'num1':num1,'num2':num2,'answer':answer})