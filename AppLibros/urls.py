from django.urls import path
from AppLibros.views import *

urlpatterns = [

    path('', inicio, name="inicio"),
    
    path("busquedaLibro/", busquedaLibro, name="busquedaLibro"),
    path("buscarLibro/", buscarLibro, name="buscarLibro"),

    path("busquedaManga/", busquedaManga, name="busquedaManga"),
    path("buscarManga/", buscarManga, name="buscarManga"),

    path("busquedaComic/", busquedaComic, name="busquedaComic"),
    path("buscarComic/", buscarComic, name="buscarComic"),

    path("LibroPeticion/", LibroPeticion, name="LibroPeticion"),
    path("MangaPeticion/", MangaPeticion, name="MangaPeticion"),
    path("ComicPeticion/", ComicPeticion, name="ComicPeticion"),

   




]