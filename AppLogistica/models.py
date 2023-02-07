from django.db import models

# Create your models here.

class Proveedor(models.Model):

    def __str__(self):

     return f"Razón Social:{self.RazonSocial}----CUIT:{self.Cuit}"


    RazonSocial=models.CharField(max_length=50)
    Cuit=models.IntegerField()
    Telefono=models.IntegerField()
    Correo=models.EmailField(max_length=25)
    CLocal=models.BooleanField()
    CMedia=models.BooleanField()

class Unidad(models.Model):
    Patente=models.CharField(max_length=10)
    TipoUnidad=models.CharField(max_length=15)
    Satelital=models.CharField(max_length=15)
    Usuario=models.CharField(max_length=20)
    Contrasena=models.CharField(max_length=25)

class Cliente(models.Model):
    RazonSocial=models.CharField(max_length=50)
    Cuit=models.IntegerField()
    Telefono=models.IntegerField()
    Correo=models.EmailField(max_length=25)
    CS=models.BooleanField(default=False)
    CN=models.BooleanField(default=False)
    CP=models.BooleanField(default=False)

class Unirte(models.Model):
    Nombre=models.CharField(max_length=20)
    Apellido=models.CharField(max_length=20)
    Telefono=models.IntegerField()
    Correo=models.EmailField(max_length=25)