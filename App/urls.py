from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('esteban', views.esteban, name="Esteban"),
    path('ana', views.ana, name= "Ana"),
    path('matias', views.matias, name='Matias'),
    path('empresa', views.empresa, name= "Empresa"),
    path('formulario', views.contacto, name="Formulario"),
    path('contactos', views.contacto, name="Contactos"),
    path('leerContacto', views.leerContacto, name="LeerContacto"),
    path('borrarContacto/<contacto_nombre>/', views.borrarContacto, name="BorrarContacto"),
    path('editarContacto/<contacto_nombre>/', views.editarContacto, name="EditarContacto"),
    path('contacto/list', views.ContactoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ContactoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ContactoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ContactoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ContactoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='App/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),


]