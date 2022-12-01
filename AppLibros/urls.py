from django.urls import path
from AppLibros.views import *

urlpatterns = [

    path('', inicio, name="inicio"),
    path("busqueda/", busquedaLibro, name="busquedaLibro"),
    path("buscar/", buscar, name="buscar"),
    path("LibroPeticion/", LibroPeticion, name="LibroPeticion"),
    path("MangaPeticion/", MangaPeticion, name="MangaPeticion"),
    path("ComicPeticion/", ComicPeticion, name="ComicPeticion"),

   




]