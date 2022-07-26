from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.http.request import QueryDict
from django.template import loader
from App.models import *
from App.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
      return render(request, 'App/inicio.html') 

@login_required
def esteban(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request,"App/Esteban.html",{"url": avatares[0].imagen.url})

@login_required
def ana(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request,"App/Ana.html",{"url": avatares[0].imagen.url})

@login_required
def matias(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request,"App/Matias.html",{"url": avatares[0].imagen.url})
      
@login_required
def empresa(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request,"App/Empresa.html",{"url": avatares[0].imagen.url})

def contacto(request):
    if request.method == 'POST':
        miformulario = Contactos(request.POST)
        print(miformulario)

        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            contacto = Contacto(nombre_completo=informacion['nombre_completo'], email=informacion['email'], telefono=informacion['telefono'], mensaje=informacion['mensaje'])  #revisar
            contacto.save()
            return render(request, 'App/inicio.html') #inicio o donde quiera
    else:
        miformulario= Contactos() 
    return render(request, 'App/contactos.html', {'miformulario':miformulario}) 

@login_required
def leerContacto(request):
    contacto = Contacto.objects.all()
    contexto = {"contacto":contacto}

    return render(request,"App/leerClientes.html",contexto)

@login_required
def borrarContacto(request, contacto_nombre):
    contacto = Contacto.objects.get(nombre_completo= contacto_nombre)
    contacto.delete()

    #vuelvo a la lista de clientes

    contactos = Contacto.objects.all()
    contexto = {"contactos":contactos}

    return render(request,"App/inicio.html",contexto)
    
@login_required
def editarContacto(request, contacto_nombre):

    #recibe el nombre del contacto que modificamos
    contacto= Contacto.objects.get(nombre_completo=contacto_nombre)

    if request.method == 'POST':
        miformulario = Contactos(request.POST) #aca llega toda la info
        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data

            contacto.nombre_completo = informacion['nombre_completo']
            contacto.email = informacion['email']
            contacto.telefono = informacion['telefono']
            contacto.mensaje = informacion['mensaje']

            contacto.save()

            return render(request, 'App/inicio.html') #inicio o donde quiera
    else:
        miformulario= Contactos(initial={'nombre_completo': contacto.nombre_completo, 'email': contacto.email, 'telefono': contacto.telefono, 'mensaje': contacto.mensaje})
    return render(request, "App/editarClientes.html", {"miformulario":miformulario, "contacto_nombre":contacto_nombre})  

class ContactoList(LoginRequiredMixin, ListView):

      model = Contacto 
      template_name = "App/contacto_list.html"



class ContactoDetalle(DetailView):

      model = Contacto 
      template_name = "App/Contacto_detail.html"


class ContactoCreacion(CreateView):

      model = Contacto 
      success_url = "App/contacto/list"
      fields = ['nombre_completo', 'email', 'telefono', 'mensaje']


class ContactoUpdate(UpdateView):

      model = Contacto 
      success_url = "App/contacto/list"
      fields  = ['nombre_completo', 'email', 'telefono', 'mensaje']


class ContactoDelete(DeleteView):

      model = Contacto 
      success_url = "App/contacto/list"
     

#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  print(1)
                  if user is not None:
                        login(request, user)

                        return render (request, "App/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        print(2)
                        return render (request, "App/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "App/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
      print(3)
      return render(request, "App/login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "App/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "App/registro.html", {"form": form})



@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "App/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "App/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})    


