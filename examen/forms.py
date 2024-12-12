from django import forms
from .models import *


class FormularioForm(forms.ModelForm):
    class Meta:
        model = promocion 
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'descuento', 'usuarios_aplicable', 'puede_tener_promociones']
    
    def clean(self):
        cleaned_data = super().clean()

        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        usuarios_aplicable= cleaned_data.get('usuarios_aplicable')
        puede_tener_promociones = cleaned_data.get('puede_tener_promociones')

        if promocion.objects.filter(nombre=nombre).exists(): #Te explico lo que hace el .exits por si acaso, lo que haces es que busca si existe en la base de datos y lo comprueba.
            self.add_error('nombre', 'Este nombre ya existe')

        if  len(descripcion) (str)  <  100:
            self.add_error('descripcion', 'La descripción debe tener al menos 100 caracteres')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            self.add_error('fecha_fin', 'La fecha de fin debe ser posterior a la fecha de inicio')

        if usuarios_aplicable (str) < 75:
            self.add_error('usuarios_aplicable', 'tienes que ser mayor de 75 años para usar la promocion')
            
        if puede_tener_promociones == False:
            self.add_error('puede_tener_promociones', 'El producto no tiene promociones') 
             
        return cleaned_data

        