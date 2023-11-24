# forms.py
from django import forms 
from .models import RegistrarForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registro_Form(forms.ModelForm):   
    class Meta:
        model = RegistrarForm
        fields = '__all__'

class register(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='contraseña_rep', widget=forms.PasswordInput)
    class Meta: 
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        