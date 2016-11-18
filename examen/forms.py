from django import forms
from .models import libro, usuario, prestamo

class libnform(forms.ModelForm):
    class Meta:
        model = libro
        fields = ('isbn', 'titulo', 'autor', 'editoria', 'pais', 'anio', 'estado')
#class prestamoForm(forms.ModelForm):
 #   class Meta:
#       model = prestamo
  #      fields = ('usuario', 'fechap', 'fechadev1','fechadev2', 'libros')

#def __init__ (self, *args, **kwargs):
#    super(prestamoForm, self).__init__(*args, **kwargs)

 #   self.fields["usuario"].widget = forms.widgets.Select()
#    self.fields["usuario"].help_text = "Seleccione usuario"
#    self.fields["usuario"].queryset = libro.objects.all()
    
#    self.fields["libros"].widget = forms.widgets.CheckboxSelectMultiple()

#    self.fields["libros"].help_text = "Ingrese los libros a prestar"
    
#    self.fields["libros"].queryset = libro.objects.all()