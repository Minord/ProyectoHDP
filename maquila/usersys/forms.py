  
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



from .models import Account

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('rol', 'phone', 'register_code')