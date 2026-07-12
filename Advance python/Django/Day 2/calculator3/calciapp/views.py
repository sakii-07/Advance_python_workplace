from django.shortcuts import render

# Create your views here.

def getaddpage(request):
    return render(request, 'add.html')

def add(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    answer = int(num1) + int(num2)
    return render(request, 'add.html', {'num1':num1,'num2':num2,'answer':answer})