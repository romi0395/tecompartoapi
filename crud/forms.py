from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

    def clean_nombre_articulo(self):
        inputNombre = self.cleaned_data['nombre_articulo']
        if len(inputNombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return inputNombre

    def clean_fono(self):
        inputFono = self.cleaned_data['fono']
        if len(inputFono) != 9:
            raise forms.ValidationError('El teléfono debe tener 9 dígitos.')
        if inputFono.find('9') != 0:
            raise forms.ValidationError('El teléfono debe empezar con 9.')
        return inputFono

    def clean_cantidad(self):
        inputCantidad = self.cleaned_data['cantidad']
        if inputCantidad < 1 or inputCantidad > 50:
            raise forms.ValidationError('La cantidad debe estar entre 1 y 50.')
        return inputCantidad

    def clean_nombre_donante(self):
        inputDonante = self.cleaned_data['nombre_donante']
        if len(inputDonante) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return inputDonante