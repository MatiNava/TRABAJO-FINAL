from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Esteban, Matias, Ana, Empresa
from App.forms import Formulario_contactate

# Create your views here.
def inicio(request):
    return render(request,'App/inicio.html')

def esteban(request):
    return render(request, 'App/Esteban.html')

def ana(request):
    return render(request, 'App/Ana.html') 

def matias(request):
    return render(request, 'App/Matias.html')

def empresa(request):
    return render(request, 'App/Empresa.html')

def formulario_contactate(request):
    if request.method == 'POST':
        miformulario = Formulario_contactate(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            formulario = Formulario_contactate (nombre_completo=informacion['nombre_completo'], email=informacion['email'], telefono=informacion['telefono'], mensaje=informacion['mensaje'])  #revisar
            formulario.save()
            return render(request, 'App/inicio.html') #inicio o donde quiera
    else:
        miformulario= Formulario_contactate() 
    return render(request, 'App/Formulario_contactate.html', {'miformulario':miformulario})           