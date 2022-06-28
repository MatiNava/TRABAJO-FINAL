from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio),
    path('esteban', views.esteban),
    path('ana', views.ana),
    path('matias', views.matias),
    path('empresa', views.empresa),
    path('formulario', views.formulario_contactate),

]