"""
URL configuration for ApiJesus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import views
from api.views import *
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('index.html', index.as_view(), name='index'),
    path('tables.html', tables.as_view(), name='tables'),
    path('Menu2.html', Menu2.as_view(), name='Menu2'),
    path('Men.html', Men.as_view(), name='Men'),
    path('Carta.html', Carta.as_view(), name='Carta'),
    path('Menu.html', Menu.as_view(), name='Menu'),
    path('forgot-password.html', forgot.as_view(), name='forgot'),
    path('register/', RegistroUsuarioView.register, name= 'register'),
    path('login/', LoginView.as_view(template_name="login.html"), name= 'login'),
    path('chart/', views.chart_view, name='chart_view'),
    
]