from django.shortcuts import render
from django.http import HttpResponse

def greet(request):
    return HttpResponse("Good Morning")

def add(request):
    return HttpResponse(10+20)

def sub(request):
    return HttpResponse(10-20)

def mul(request):
    return HttpResponse(10*20)

def div(request):
    return HttpResponse(10/2)