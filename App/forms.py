from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dataclasses import fields


class Form_contacto(forms.Form):
    nombre_completo= forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    mensaje = forms.CharField()

class Contactos(forms.Form):
    nombre_completo= forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    mensaje = forms.CharField()


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    #extendemos el contenido de el formulario viejo agregando dos campos más
    # last_name: forms.CharField()
    # first_name: forms.CharField()

    class Meta:
        model = User                                               #agregamos los campos
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username': 'nombre', 'email':'correo','last_name': 'apellido', 'first_name':'nombre'}
        help_texts= {k:"" for k in fields}

#La clase meta es una clase interna en los modelos de Django.
#Que contienen opciones Meta (metadatos) que se utilizan para
#cambiar el comportamiento de los campos de su modelo,
#como cambiar las opciones de orden, si el modelo es abstracto o no,
#versiones singulares y plurales del nombre, etc. 

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}    