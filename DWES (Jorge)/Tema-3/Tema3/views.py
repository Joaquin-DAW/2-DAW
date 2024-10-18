from django.shortcuts import render
from django.db.models import Q
from .models import Libro, Cliente

# Create your views here.

def index(request):
    return render(request,'index.html') 

def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.all()
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request,id_libro):
    QSlibro = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libro = QSlibro.get(id=id_libro)
    return render(request, 'libro/libro.html',{"libro_mostrar":libro})

def dame_libros_fecha(request, anyo_libro, mes_libro):
    libros = Libro.objects.prefetch_related("autores").select_related("biblioteca")
    libros = libros.filter(fecha_publicacion__year=anyo_libro, fecha_publicacion__month=mes_libro)
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libros_idioma(request, tipo):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros.filter(Q(tipo=tipo) | Q(tipo="ES")).order_by("fecha_publicacion")
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libros_biblioteca(request,id_biblioteca,texto_libro):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.filter(biblioteca=id_biblioteca).filter(descripcion__contains=texto_libro).order_by("-nombre")
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_ultimo_cliente_libro(request,libro):
    cliente = Cliente.objects.filter(prestamo__libro=libro).order_by("-prestamo__fecha_prestamo")[:1].get()
    cliente = (Cliente.objects.raw("SELECT * FROM biblioteca_cliente c "
                               + " JOIN biblioteca_prestamo p ON p.libro_id = %s "   
                               + " ORDER BY p.fecha_prestamo DESC "
                               ,[libro])[0]
               )
    
    return  render(request, 'cliente/cliente.html',{"cliente":cliente})