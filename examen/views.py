from django.shortcuts import render

#librería para manejar el envío de mensajes
from django.contrib import messages
###from .forms import PeliculaForm
from .models import libro, usuario, prestamo


def lista(request):
    return render(request, 'examen/lista.html', {})
