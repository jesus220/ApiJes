from telnetlib import LOGOUT
from rest_framework.views import APIView
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import Registro_Form
from .forms import register as registros
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from .models import General
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect

# from django.conf import settings
# from api.models import Product
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages




class Home (APIView):
    template_name="Men.html"
    def get(self, request):
        return render(request,self.template_name)
    
def index(request):
    # Lógica de la vista, si es necesaria
    return render(request, 'index.html')
    
class Carta (APIView):
    template_name="Carta.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Bebida (APIView):
    template_name="Bebidas.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Menu2 (APIView):
    template_name="Menu2.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Men (APIView):
    template_name="Men.html"
    def get(self, request):
        return render(request,self.template_name)
    
class login (APIView):
    template_name="login.html"
    def get(self, request):
        return render(request,self.template_name)  
      
class chart_view (APIView):
    template_name="chart.html"
    def get(self, request):
        return render(request,self.template_name)   
      
class tables (APIView):
    template_name="tables.html"
    def get(self, request):
        return render(request,self.template_name)
        
class forgot (APIView):
    template_name="forgot-password.html"
    def get(self, request):
        return render(request,self.template_name)
    
class register(APIView):
    template_name="register.html"
    def get(self, request):
        return render(request,self.template_name)
    

# Create your views here. estas xd, mira:
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}!")
            # Redirigir según el tipo de usuario
            if user.is_staff:
                # Mensaje en consola
                print("Redirigiendo a la vista de administrador")
                return redirect("index")  # Cambia "admin_dashboard" a tu URL de administrador
            else:
                # Mensaje en consola
                print("Tipo de usuario no válido. Redirigiendo a la vista de inicio de sesión")
                return redirect("Men")
        else:
            messages.error(request, "Credenciales no válidas.")
            # Mensaje en consola
            print("Credenciales no válidas. Redirigiendo a la vista de inicio de sesión")

    return render(request, 'login.html')
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = "Los datos son incorrectos. Por favor, inténtalo de nuevo."
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')



from urllib import request
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, password=password)
                    if user is not None:
                        # Envío del correo con formato HTML
                        subject = 'Registro Exitoso'
                        from_email = 'jesus480b@gmail.com'  # Cambiar por tu dirección de correo
                        to_email = [email]
                        
                        # Renderiza el template HTML del correo
                        html_content = render_to_string('email-user.html', {
                            'username': username,
                            'password': password,
                        })
                        
                        text_content = strip_tags(html_content)  # Elimina el HTML para usuarios que no admiten HTML
                        
                        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        
                        # Una vez que se ha creado el usuario, redirige a la página de inicio de sesión
                        return redirect('login_view')
                else:
                    error_message = "El correo electrónico ya está en uso."
                    return render(request, 'register.html', {'error_message': error_message})
            else:
                error_message = "El nombre de usuario ya existe."
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'register.html', {'error_message': error_message})

    return render(request, 'register.html')


def salir(request):
    logout(request)
    messages.success(request, "Tu sesión se ha cerrado correctamente.")
    return redirect("login_view")


    


def chart_view(request):
    #Precios
    precios1 = General.objects.filter(precios="$250").count()
    precios2 = General.objects.filter(precios="$300").count()
    precios3 = General.objects.filter(precios="$350").count()
    precios4 = General.objects.filter(precios="$400").count()
    
    #Empanadas
    empanadas1 = General.objects.filter(empanadas="Chistorra").count()
    empanadas2 = General.objects.filter(empanadas="Queso").count()
    empanadas3 = General.objects.filter(empanadas="Elote con queso").count()
    empanadas4 = General.objects.filter(empanadas="Espinaca con queso").count()
    
    #Cortes
    cortes1 = General.objects.filter(cortes="Arrachera").count()
    cortes2 = General.objects.filter(cortes="Rib eye").count()
    cortes3 = General.objects.filter(cortes="Churrasco").count()
    cortes4 = General.objects.filter(cortes="Asado de tira").count()
    
    #Guarniciones
    guarniciones1 = General.objects.filter(guarniciones="Chinchulines").count()
    guarniciones2 = General.objects.filter(guarniciones="Mollejas").count()
    guarniciones3 = General.objects.filter(guarniciones="Chistorra").count()
    guarniciones4 = General.objects.filter(guarniciones="Chorizo argentino").count()
    
    
    #Postres
    postres1 = General.objects.filter(postres="Strudel de manzana").count()
    postres2 = General.objects.filter(postres="Pastelito de chocolate").count()
    postres3 = General.objects.filter(postres="Durazno con cremas").count()
    postres4 = General.objects.filter(postres="Alfajor").count()
    
    
    #Salsa Pastas
    salsapastas1 = General.objects.filter(salsapastas="salsa boloñesa").count()
    salsapastas2 = General.objects.filter(salsapastas="Salsa pesto").count()
    salsapastas3 = General.objects.filter(salsapastas="Salsa burro").count()
    salsapastas4 = General.objects.filter(salsapastas="Salsa alfredo").count()
      
    
    #Alcohol
    alcohol1 = General.objects.filter(alcohol="Tequila").count()
    alcohol2 = General.objects.filter(alcohol="Vodka").count()
    alcohol3 = General.objects.filter(alcohol="Whisky").count()
    alcohol4 = General.objects.filter(alcohol="no tomo").count()
    
    
    #Cervezas
    cervezas1 = General.objects.filter(cervezas="Indio").count()
    cervezas2 = General.objects.filter(cervezas="Tecate").count()
    cervezas3 = General.objects.filter(cervezas="Heineken").count()
    cervezas4 = General.objects.filter(cervezas="No tomo").count()
    
    
    #Refresco
    refrescos1 = General.objects.filter(refrescos="Pepsi").count()
    refrescos2 = General.objects.filter(refrescos="Mirinda").count()
    refrescos3 = General.objects.filter(refrescos="Manzanita").count()
    refrescos4 = General.objects.filter(refrescos="7up").count()
    
    
     #Cafes
    cafes1 = General.objects.filter(cafes="Americano").count()
    cafes2 = General.objects.filter(cafes="Capuchino").count()
    cafes3 = General.objects.filter(cafes="Expreso").count()
    cafes4 = General.objects.filter(cafes="No me gusta el café").count()
    

    return render(request, 'chart.html', context = {
        'precios1': precios1,
        'precios2': precios2,
        'precios3': precios3,
        'precios4': precios4,
        
        
        'empanadas1': empanadas1, 
        'empanadas2': empanadas2, 
        'empanadas3': empanadas3, 
        'empanadas4': empanadas4, 
        
        
        'cortes1': cortes1, 
        'cortes2': cortes2, 
        'cortes3': cortes3, 
        'cortes4': cortes4,   
        
        'guarniciones1': guarniciones1,
        'guarniciones2': guarniciones2,
        'guarniciones3': guarniciones3,
        'guarniciones4': guarniciones4,
        
        
        'postres1': postres1,
        'postres2': postres2,
        'postres3': postres3,
        'postres4': postres4,
        
        
        'salsapastas1': salsapastas1,
        'salsapastas2': salsapastas2,
        'salsapastas3': salsapastas3,
        'salsapastas4': salsapastas4,  
        
        
        'alcohol1': alcohol1,
        'alcohol2': alcohol2,
        'alcohol3': alcohol3,
        'alcohol4': alcohol4, 
        
        
        'cervezas1': cervezas1,
        'cervezas2': cervezas2,
        'cervezas3': cervezas3,
        'cervezas4': cervezas4,      
        
        
        'refrescos1': refrescos1,
        'refrescos2': refrescos2,
        'refrescos3': refrescos3,
        'refrescos4': refrescos4,   
                                        
        'cafes1': cafes1,
        'cafes2': cafes2,
        'cafes3': cafes3,
        'cafes4': cafes4, 
    }
    )
    


#def salir(request):
#    logout(request)
#    return redirect('login')

