from django.db import models
from django.contrib import admin

class libro(models.Model):

    isbn = models.CharField(max_length=13)
    titulo  =   models.CharField(max_length=60)
    portada = models.CharField(max_length=13)
    autor  =   models.CharField(max_length=100)
    editoria  =   models.CharField(max_length=30)
    pais  =   models.CharField(max_length=50)
    anio = models.IntegerField()
    
    #el estado es para identificar si esta prestado o no el libro.
    estado = models.BooleanField()
    
    def __str__(self):
        return self.titulo

#el enunciado indica que el prestamista es un usuario
class usuario(models.Model):
    dpi = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)

    libros   = models.ManyToManyField(libro, through='prestamo')
    def __str__(self):
        return self.nombre

#tabla prestamo para llevar el control de cada prestamo
class prestamo (models.Model):
    tlibro = models.ForeignKey(libro, on_delete=models.CASCADE)
    tusuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    
    fechaprestamo=models.DateField()
    fechadevp=models.DateField()
    fechadevr=models.DateField()


class prestamoInLine(admin.TabularInline):
    model = prestamo
    extra = 1

class libroAdmin(admin.ModelAdmin):
    inlines = (prestamoInLine,)

class usuarioAdmin (admin.ModelAdmin):
    inlines = (prestamoInLine,)