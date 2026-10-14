from django.shortcuts import render, redirect
from .models import Mueble
from .forms import MuebleForm
from .serializers import MuebleSerializer
from rest_framework import viewsets

# Create your views here.
def inicio(request):
    return render(request,"paginas/inicio.html")

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def muebles(request):
    muebles = Mueble.objects.all()

    return render(request,'muebles/index.html',{'muebles':muebles})

def crear(request):
    formulario = MuebleForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('muebles')
    return render(request,'muebles/crear.html',{'formulario':formulario})

def editar(request, id):
    mueble = Mueble.objects.get(id=id)
    formulario = MuebleForm(request.POST or None, request.FILES or None, instance=mueble)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('muebles')
    return render(request,'muebles/editar.html',{'formulario':formulario})

def eliminar(request, id):
    mueble = Mueble.objects.get(id=id)
    mueble.delete()
    return redirect('muebles')

class MuebleViewSet(viewsets.ModelViewSet):
    queryset = Mueble.objects.all()
    serializer_class = MuebleSerializer