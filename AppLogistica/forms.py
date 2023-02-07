from django import forms

# Create your forms here.

class FormularioProveedor(forms.Form):
    RazonSocial=forms.CharField(max_length=50)
    Cuit=forms.IntegerField()
    Telefono=forms.IntegerField()
    Correo=forms.EmailField(max_length=25)
    CLocal=forms.BooleanField()
    CMedia=forms.BooleanField()

class FormularioUnidad(forms.Form):
    Patente=forms.CharField(max_length=10)
    TipoUnidad=forms.CharField(max_length=15)
    Satelital=forms.CharField(max_length=20)
    Usuario=forms.CharField(max_length=20)
    Contrasena=forms.CharField(max_length=25)

class FormularioCliente(forms.Form):
    RazonSocial=forms.CharField(max_length=50)
    Cuit=forms.IntegerField()
    Telefono=forms.IntegerField()
    Correo=forms.EmailField(max_length=25)
    CS=forms.BooleanField()
    CN=forms.BooleanField()
    CP=forms.BooleanField()

class FormularioUnirte(forms.Form):
    Nombre=forms.CharField(max_length=20)
    Apellido=forms.CharField(max_length=20)
    Telefono=forms.IntegerField()
    Correo=forms.EmailField(max_length=25)