import email
from msilib.schema import ListView
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Matias(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion} "

class Esteban(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion} "

class Ana(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion} " 

class Empresa(models.Model):
    nombre = models.CharField(max_length=40)
    grupo = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Grupo: {self.grupo} "  

class Contacto(models.Model):
    nombre_completo= models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=30)

    def __str__(self):
        return (f"Nombre: {self.nombre_completo} - Email: {self.email} - Telefono: {self.telefono} - Mensaje: {self.mensaje} ") 

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)        
