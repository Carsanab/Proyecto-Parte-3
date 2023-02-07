from django.shortcuts import render
from django.http import HttpResponse
from AppLogistica.models import*
from AppLogistica.forms import*
from AppLogistica.views import*

# Create your views here.
def Inicio(request):

    return render(request,"AppLogistica/Inicio.html")


def VerProveedor(request):

    todos=Proveedor.objects.all() # sacando todos los proveedores de la base de datos
    return render(request,"AppLogistica/VerProveedor.html",{'todos':todos})


def VerUnidad(request):
    todos=Unidad.objects.all() # sacando todas las unidades de la base de datos
    return render(request,"AppLogistica/VerUnidad.html",{'todos':todos})


def VerCliente(request):
    todos=Cliente.objects.all() # sacando todas las unidades de la base de datos
    return render(request,"AppLogistica/VerCliente.html",{'todos':todos})

def Unirte(request):

    return render(request,"AppLogistica/Unirte.html")
    

# Vistas para formularios
def AgregarProveedor(request): #Formulario para agregar un proveedor

    if request.method=="POST":
        MiFormulario=FormularioProveedor(request.POST)
        
        if MiFormulario.is_valid():
            informacion=MiFormulario.cleaned_data
            Prov=Proveedor(RazonSocial=informacion['RazonSocial'],Cuit=informacion['Cuit'],
                           Telefono=informacion['Telefono'],Correo=informacion['Correo'],
                           CLocal=informacion['CLocal'],
                           CMedia=informacion['CMedia'])
            Prov.save()
            return render(request,"AppLogistica/Inicio.html")
    else:
        MiFormulario=FormularioProveedor()

    return render(request,"AppLogistica/FormularioProveedor.html",{"MiFormulario":MiFormulario}) 
        
def AgregarUnidad(request): #formulario para registrar una unidad

    if request.method=="POST":
        MiFormulario=FormularioUnidad(request.POST)
        
        if MiFormulario.is_valid():
            informacion=MiFormulario.cleaned_data
            Unid=Unidad(Patente=informacion['Patente'],TipoUnidad=informacion['TipoUnidad'],
                           Satelital=informacion['Satelital'],Usuario=informacion['Usuario'],
                           Contrasena=informacion['Contrasena'])
                           
            Unid.save()
            return render(request,"AppLogistica/Inicio.html")
    else:
        MiFormulario=FormularioUnidad()

    return render(request,"AppLogistica/FormularioUnidad.html",{"MiFormulario":MiFormulario}) 

def AgregarCliente(request): #formulario para registrar un cliente

    if request.method=="POST":
        MiFormulario=FormularioCliente(request.POST)
        
        if MiFormulario.is_valid():
            informacion=MiFormulario.cleaned_data
            Client=Cliente(RazonSocial=informacion['RazonSocial'],Cuit=informacion['Cuit'],
                           Telefono=informacion['Telefono'],Correo=informacion['Correo'],
                           CS=informacion['CS'],CN=informacion['CN'],CP=informacion['CP'])
                           
            Client.save()
            return render(request,"AppLogistica/Inicio.html")
    else:
        MiFormulario=FormularioCliente()

    return render(request,"AppLogistica/FormularioCliente.html",{"MiFormulario":MiFormulario})

def UnirteAlEquipo(request): #formulario para registrar un cliente

    if request.method == "POST":
        MiFormulario=FormularioUnirte(request.POST)
        
        if MiFormulario.is_valid():
            informacion=MiFormulario.cleaned_data
            Unirt=Unirte(Nombre=informacion['Nombre'],Apellido=informacion['Apellido'],
                           Telefono=informacion['Telefono'],Correo=informacion['Correo'])
                           
            Unirt.save()
            
            return render(request,"AppLogistica/Inicio.html")
    else:
        MiFormulario=FormularioUnirte()

    return render(request,"AppLogistica/Unirte.html",{"MiFormulario":MiFormulario})  

def BuscarProveedor(request):

    return render(request,"AppLogistica/BuscarProveedor.html")


def resultados(request):

    ProveedorBusqueda=request.GET['RazonSocial']
    ResultadosProveedor=Proveedor.objects.filter(RazonSocial__icontains=ProveedorBusqueda)
    
    return render(request,"AppLogistica/resultados.html",{"PROVEEDOR BUSCADO": {ProveedorBusqueda},"RESULTADOS":{ResultadosProveedor}})

