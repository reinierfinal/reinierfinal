from django.conf.urls import url
from .import views


#para llamar a nuestra página para insertar tenemos que invocar la dirección /prestamo/nuevo

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.lista),
    url(r'^libro/nuevo/$', views.libn, name='libn'),
    #url(r'^/prestamo/nuevo/$', views.prestamo_nuevo, name='prestamo_nuevo'),
    ]