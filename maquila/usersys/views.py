from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import CreateUserForm, CreateAccountForm

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST, instance=request.user)
        account_form = CreateAccountForm(request.POST, instance=request.user.account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('login')
    else:
        user_form = CreateUserForm(instance=request.user)
        account_form = CreateAccountForm(instance=request.user.account)
    return render(request, 'register.html', {
        'user_form': user_form,
        'account_form': account_form
    })

def logout(request):
    return "LogOut"

def createcode(request):
    return render(request, 'createcode.html')
