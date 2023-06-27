from django.db import models

# Create your models here.

from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator

# Create your models here.

class Bono(models.Model):
    ticker = models.CharField(max_length=5, validators=[MaxLengthValidator(5), MinLengthValidator(5)])
    descripcion = models.CharField(max_length=30)
    cupon = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    emisor = models.CharField(max_length=30)
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()

class Accion(models.Model):
    ticker = models.CharField(max_length=4, validators=[MaxLengthValidator(4), MinLengthValidator(4)])
    descripcion = models.CharField(max_length=30)
    Empresa = models.CharField(max_length=20)

class Futuro(models.Model):
    ticker = models.CharField(max_length=10, validators=[MaxLengthValidator(9), MinLengthValidator(9)])
    descripcion = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()


