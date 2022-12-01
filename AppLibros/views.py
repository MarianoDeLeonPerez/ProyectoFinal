from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppLibros.forms import *

# Create your views here.

def inicio(request):
    
    return render (request, "AppLibros/inicio.html")


def busqueda(request):

    return render (request, 'AppLibros/busqueda.html')



def peticion(request):

    return render (request, 'AppLibros/peticion.html')    

def LibroPeticion(request):

    if request.method=="POST":

        form=PeticionForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            autor=informacion["autor"]
            libro= Libros(nombre=nombre, autor=autor)
            libro.save()
            return render (request, "AppLibros/inicio.html", {"mensaje": "PETICION REALIZADA CORRECTAMENTE"})
    else:
        formulario=PeticionForm()


    return render (request, "AppLibros/libropeticion.html", {"form":formulario})

def MangaPeticion(request):

    if request.method=="POST":

        form=PeticionForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            autor=informacion["autor"]
            manga=Mangas(nombre=nombre, autor=autor)
            manga.save()
            return render (request, "AppLibros/inicio.html", {"mensaje": "PETICION REALIZADA CORRECTAMENTE"})
    else:
        formulario=PeticionForm()


    return render (request, "AppLibros/mangapeticion.html", {"form":formulario})



def ComicPeticion(request):

    if request.method=="POST":

        form=PeticionForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            autor=informacion["autor"]
            comic= Libros(nombre=nombre, autor=autor)
            comic.save()
            return render (request, "AppLibros/inicio.html", {"mensaje": "PETICION REALIZADA CORRECTAMENTE"})
    else:
        formulario=PeticionForm()


    return render (request, "AppLibros/comicpeticion.html", {"form":formulario})    

def busquedaLibro(request):

    return render(request, "AppLibros/busquedaLibro.html")

def buscar(request):

    if request.GET["nombre"]:

        libro=request.GET["nombre"]

        libros=Libros.objects.filter(nombre__icontains=libro)
        return render(request,"AppLibros/resultadosBusqueda.html", {"libros":libros} )
    else:
        return render(request, "AppLibros/busquedaLibro.html", {"mensaje":"Nombre no valido o no se encuentra"})


