from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import Registro_Form
from .forms import register as registros
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from .models import General
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
# from django.conf import settings
# from api.models import Product




class Home (APIView):
    template_name="Menu.html"
    def get(self, request):
        return render(request,self.template_name)
    
class index (APIView):
    template_name="index.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Menu2 (APIView):
    template_name="Menu2.html"
    def get(self, request):
        return render(request,self.template_name)
    
class Menu (APIView):
    template_name="Menu.html"
    def get(self, request):
        return render(request,self.template_name)
    
class succes (APIView):
    template_name="success.html"
    def get(self, request):
        return render(request,self.template_name)
    
class cancel (APIView):
    template_name="cancel.html"
    def get(self, request):
        return render(request,self.template_name)
    
class redirect (APIView):
    template_name="redirect.html"
    def get(self, request):
        return render(request,self.template_name)
    
class menu (APIView):
    template_name="Menu.html"
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
    

class RegistroUsuarioView(HttpRequest):
    def index(request):
        Usuario = Registro_Form
        return render(request, "register.html", {"form":Usuario})
    def procesar_formulario(request):
        Usuario = Registro_Form(request.POST)
        if Usuario.is_valid():
            Usuario.save()
            Usuario = Registro_Form()
        return render(request, "login.html", {"form":Usuario, "mensaje":"OK"})
    def register(request):
        if request.method == 'POST':
            form = registros(request.POST)
            if form.is_valid():
                form.save()
                send_mail(
                'Bienvenido',    # Asunto del correo
                'Felicidades te has registrado con exito',    # Cuerpo del correo
                'jesus480@gmail.com',   # Dirección de correo remitente
                [request.POST['email']],  # Lista de direcciones de correo de destinatarios
                fail_silently=False,     # Si se establece en True, los errores en el envío de correo no generarán una excepción
                )
                return redirect('login')   
        else: 
            form = registros()
        context = { 'form' : form}
        return render(request, 'register.html', context) 
    


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
    
# def process_payment(request):
#     # Configurar las credenciales de PayPal
#     paypal_mode = settings.PAYPAL_MODE
#     paypal_client_id = settings.PAYPAL_CLIENT_ID
#     paypal_secret = settings.PAYPAL_SECRET

#     # Configurar las credenciales de PayPal
#     Payment.client_id = paypal_client_id
#     Payment.client_secret = paypal_secret

#     # Crear el pago
#     payment = Payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal",
#         },
#         "redirect_urls": {
#             "return_url": request.build_absolute_uri(reverse('payment_success')),
#             "cancel_url": request.build_absolute_uri(reverse('payment_cancel')),
#         },
#         "transactions": [{
#             "item_list": {
#                 "items": [{
#                     "name": "Producto de ejemplo",
#                     "sku": "123",
#                     "price": "10.00",
#                     "currency": "USD",
#                     "quantity": 1,
#                 }],
#             },
#             "amount": {
#                 "total": "10.00",
#                 "currency": "USD",
#             },
#             "description": "Descripción del pago de ejemplo",
#         }],
#     })

#     if payment.create():
#         # Redireccionar al usuario a la URL de aprobación de PayPal
#         for link in payment.links:
#             if link.method == "REDIRECT" and link.rel == "approval_url":
#                 return render(request, 'payment/redirect.html', {'redirect_url': link.href})
#     else:
#         return HttpResponse('Error al crear el pago en PayPal')
    
    
# def payment_success(request):
#     return render(request, 'payment/success.html')

# def payment_cancel(request):
#     return render(request, 'payment/cancel.html')

#def salir(request):
#    logout(request)
#    return redirect('login')

