from django.forms import (
    TextInput,
    NumberInput,
    ModelForm,
    ClearableFileInput
)
from .models import Producto


class FormularioProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_artista','nombre_album', 'año', 'precio', 'img', 'tipo' ]
        widgets = {
            'nombre_artista': TextInput(attrs={'class': 'form-control'}),
            'nombre_album': TextInput(attrs={'class': 'form-control'}),
            'año': NumberInput(attrs= {'class': 'form-control'}),
            'precio': TextInput(attrs={'class': 'form-control'}),
            'img': ClearableFileInput(attrs={'class': 'form-control-file'}),
            'tipo': TextInput(attrs = {'class': 'form-control'}),
        }