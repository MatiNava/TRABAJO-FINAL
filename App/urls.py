from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio),
    path('familia', views.familiares),
]