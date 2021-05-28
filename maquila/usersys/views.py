from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def createcode(request):
    return render(request, 'createcode.html')
