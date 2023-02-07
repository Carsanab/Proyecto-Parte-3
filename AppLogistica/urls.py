from django.urls import path
from AppLogistica.views import*
urlpatterns = [
    path('Inicio/',Inicio,name="inicio"),
    path('VerProveedor/',VerProveedor,name="proveedores"),
    path('VerUnidad/',VerUnidad,name="unidades"),
    path('VerCliente/',VerCliente,name="clientes"),
    path('Unirte/',Unirte,name="equipoTrabajo"),
    path('NuevoProveedor/', AgregarProveedor,name="proveedornuevo"),
    path('NuevaUnidad/', AgregarUnidad,name="unidadnueva"),
    path('NuevoCliente/',AgregarCliente,name="clientenuevo"),
    path('UnirteAlEquipo/',UnirteAlEquipo,name="unirte"),

    path('BuscarProveedor/',BuscarProveedor),
    path('resultados/',resultados,name="Resultados")
    

]