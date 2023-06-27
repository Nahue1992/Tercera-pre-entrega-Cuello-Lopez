from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator

class CrearBonoFormulario(forms.Form):
    ticker = forms.CharField(max_length=5, validators=[MaxLengthValidator(5), MinLengthValidator(5)])
    descripcion = forms.CharField(max_length=30, required=False)
    cupon = forms.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    emisor = forms.CharField(max_length=30)
    fecha_emision = forms.DateField()
    fecha_vencimiento = forms.DateField()


class CrearAccionFormulario(forms.Form):
    ticker = forms.CharField(max_length=4)
    descripcion = forms.CharField(max_length=30, required=False)
    Empresa = forms.CharField(max_length=20)

class CrearFuturoFormulario(forms.Form):
    ticker = forms.CharField(max_length=9, validators=[MaxLengthValidator(9), MinLengthValidator(9)])
    descripcion = forms.CharField(max_length=30)
    fecha_vencimiento = forms.DateField()


class BuscarEspeciesFormulario(forms.Form):
    ticker = forms.CharField(required=False)
