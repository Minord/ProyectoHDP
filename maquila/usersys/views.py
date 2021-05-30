from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import CreateUserForm, CreateAccountForm

from django.contrib.auth import authenticate, login, logout

from .models import Account, AuthCode

import secrets
from datetime import datetime
from datetime import timedelta



def login_user(request):
    if request.user.is_authenticated:
        return rol_depended_redirect(request.user)

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return rol_depended_redirect(user)
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
            return rol_depended_redirect(request.user)

    if request.method == 'POST':
        #Requierements for registration.
        account_category = request.POST.get('rol')
        code_text = request.POST.get('register_code')
        authCode = AuthCode.objects.filter(code = code_text)

        equal_category = False

        if len(authCode) > 0:
            equal_category = account_category == authCode.first().category
        
        if len(authCode) > 0 and equal_category:
            #Create the Register and by consecuence a void account
            user_form = CreateUserForm(request.POST)
            user = None
            if user_form.is_valid():
                user = user_form.save()
            #Get the acount and update the data
            print(user)
            account = Account.objects.get(user=user)
            account_form = CreateAccountForm(request.POST, instance=account)
            if account_form.is_valid():
                account_form.save()    

            return redirect('login')
        else:
            if not equal_category:
                messages.info(request, 'Codigo Categoria Incorrecta')
            else:
                messages.info(request, 'Codigo Incorrecto')
            
    else:        
        user_form = CreateUserForm()
        account_form = CreateAccountForm()
        return render(request, 'register.html', {
            'user_form': user_form,
            'account_form': account_form
        })
    user_form = CreateUserForm()
    account_form = CreateAccountForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'account_form': account_form
    })

def logout_user(request):
    logout(request)
    return redirect('login')

def createcode(request):

    if request.method == 'POST':
        #Generar El Codigo Aqui
        account = Account.objects.get(user=request.user)
        account_type = account.rol

        if account_type == 'administrator':
            code = secrets.token_hex(6)
            category = request.POST.get('category')
            date_created = datetime.today() 
            date_expired = datetime.today() + timedelta(days=1)
            code_register = AuthCode.objects.create(code=code, category = category,
                                    date_created = date_created, date_expired = date_expired)
            code_register.save()
            messages.info(request, code)
        else: 
            messages.info(request, 'Este usuario no es de tipo administrador')

    return render(request, 'createcode.html')


def rol_depended_redirect(user):
    account = Account.objects.get(user=user)
    account_type = account.rol

    if account_type == 'administrator':
        return redirect('pedidos_admin')

    elif account_type == 'worker':
        return redirect('actividades_worker')

    elif account_type == 'client':
        return redirect('pedidos_client')
    return redirect('/')