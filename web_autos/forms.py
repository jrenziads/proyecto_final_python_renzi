from django import forms
from .models import Car, Brand, Owner

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']
        labels = {
            'name': 'Nombre',
            'country': 'País',
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price']
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'year': 'Año',
            'price': 'Precio',
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'car']
        labels = {
            'name': 'Nombre',
            'car': 'Vehiculo',
        }

class SearchForm(forms.Form):
    query = forms.CharField(
        label='Buscar',
        max_length=100,
        error_messages={
            'required': 'Este campo es obligatorio',
        }
    )