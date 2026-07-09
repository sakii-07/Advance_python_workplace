from django.shortcuts import render

# Create your views here.

def getaddpage(request):
    return render(request, 'add.html')

def add(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) + int(num2)

    return render(request, 'add.html', {'num1':num1,'num2':num2,'answer':answer})

def getsubpage(request):
    return render(request, 'sub.html')

def sub(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) - int(num2)

    return render(request, 'sub.html', {'num1':num1,'num2':num2,'answer':answer})

def getmulpage(request):
    return render(request, 'mul.html')

def mul(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) * int(num2)

    return render(request, 'mul.html', {'num1':num1,'num2':num2,'answer':answer})

def getdivpage(request):
    return render(request, 'div.html')

def div(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) / int(num2)

    return render(request, 'div.html', {'num1':num1,'num2':num2,'answer':answer})

def getfloorpage(request):
    return render(request, 'floor.html')

def floor(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) // int(num2)

    return render(request, 'floor.html', {'num1':num1,'num2':num2,'answer':answer})