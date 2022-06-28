from django import forms

class Formulario_contactate(forms.Form):
    nombre_completo= forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    mensaje = forms.CharField()
