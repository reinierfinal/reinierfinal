from django.contrib import admin
from .models import libro, usuario, prestamo

admin.site.register(libro)
admin.site.register(usuario)
admin.site.register(prestamo)