from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Esteban, Matias, Ana, Empresa

# Create your views here.
def inicio(request):
    return render(request,'App/inicio.html')

def familiares(request):
    return render(request, 'App/familiares.html')