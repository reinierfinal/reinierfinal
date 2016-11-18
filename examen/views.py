from django.shortcuts import render

#librería para manejar el envío de mensajes
#from django.contrib import messages
from .forms import libnform
from .models import libro, usuario, prestamo


def lista(request):
    return render(request, 'examen/lista.html', {})

def libn(request):
    if request.method == "POST":
        form = libnform(request.POST)
        if form.is_valid():
            lib = form.save(commit=False)
            lib.save()
    else:
        form = libnform()
    return render(request, 'examen/nuevo.html', {'form': form})

#def prestamo_nuevo(request):
#    if request.method == "POST":
#        formulario = prestamoForm(request.POST)
#        if formulario.is_valid():
#            ttusuario = request.POST.get('usuario') 
#usuario.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
 #           
#            for libro_id in request.POST.getlist('libros'):
#                tprestamo = prestamo(tlibro_id=libro_id, tusuario_id = ttusuario, fechaprestamo=formulario.cleaned_data['fechap'], fechadevp=formulario.cleaned_data['fechadev1'], fechadevr=formulario.cleaned_data['fechadev2'])
 #               tprestamo.save()
            #messages.add_message(request, 
            #messages.SUCCESS, 'Prestamo realizado')
#    else:
#        formulario = prestamoForm()
#    return render(request, 'prestamo/nuevo.html', {'formulario': formulario})