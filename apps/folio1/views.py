from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos
# Create your views here.


def index(request):
    datos = Datos.objects.all()[0]
    nombre = datos.nombre
    apellido = datos.apellido
    return render(request ,'index.html',{'nombre':nombre,'apellido':apellido})
