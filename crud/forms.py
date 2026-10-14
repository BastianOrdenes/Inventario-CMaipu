from django import forms
from .models import Mueble

class MuebleForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'

    def clean_nombre(self):
        inputNombre = self.cleaned_data.get('nombre')
        if inputNombre:
            if len(inputNombre.strip()) < 3:
                raise forms.ValidationError("El nombre del mueble debe tener al menos 3 caracteres.")
            if len(inputNombre.strip()) > 50:
                raise forms.ValidationError("El nombre del mueble no puede superar los 50 caracteres.")
        return inputNombre