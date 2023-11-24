from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RegistrarForm(models.Model):
    Id_login= models.AutoField(primary_key=True)
    nombre_us= models.CharField(max_length=100,db_column='nombre_us')
    apellidos_us = models.CharField(max_length=100,db_column='apellidos_us')
    correo_us =models.CharField(max_length=100,db_column='correo_us')
    contraseña=models.CharField(max_length=100,db_column='contraseña_us')
    rep_contra=models.CharField(max_length=100,db_column='rep_contra')
    class Meta:
        db_table='Registrar'

        
class General(models.Model):
    Id_general = models.AutoField(primary_key=True)
    precios= models.CharField(max_length=100,db_column='Precios')
    empanadas= models.CharField(max_length=100,db_column='Empanadas')
    cortes= models.CharField(max_length=100,db_column='Cortes')
    guarniciones= models.CharField(max_length=100,db_column='Guarniciones')
    postres= models.CharField(max_length=100,db_column='Postres')
    salsapastas= models.CharField(max_length=100,db_column='SalsaPasta')
    alcohol= models.CharField(max_length=100,db_column='Alcohol')
    cervezas= models.CharField(max_length=100,db_column='Cervezas')
    refrescos= models.CharField(max_length=100,db_column='Refrescos')
    cafes= models.CharField(max_length=100,db_column='Cafes')
    class Meta:
        db_table="General"
        
        
class Product(models.Model):
    
    name=models.CharField(max_length=225)
    description= models.TextField()
    price= models.IntegerField()
    image=models.URLField(blank=True, null=True)
    
    def __str__(self) :
        return self.name
    
