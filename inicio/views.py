from django.shortcuts import render
from inicio.forms import CrearAccionFormulario, CrearBonoFormulario, CrearFuturoFormulario
from inicio.models import Bono, Accion, Futuro

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_bono(request):
    mensaje = ''
    if request.method == 'POST':
        formulario = CrearBonoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            bono = Bono(ticker=info['ticker'], descripcion=info['descripcion'], cupon=info['cupon'],
                        emisor=info['emisor'], fecha_emision=info['fecha_emision'],
                        fecha_vencimiento=info['fecha_vencimiento'])
            bono.save()
            mensaje = f'Se creó el bono {bono.ticker}'
        else:
            return render(request, 'inicio/crear_bono.html', {'formulario': formulario})

    formulario = CrearBonoFormulario()
    return render(request, 'inicio/crear_bono.html', {'formulario': formulario, 'mensaje': mensaje})

def crear_accion(request):

    mensaje = ''
    if request.method == 'POST':
        formulario = CrearAccionFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            accion = Accion(ticker=info['ticker'], descripcion=info['descripcion'], Empresa=info['Empresa'])
            accion.save()
            mensaje = f'Se creó la acción {accion.ticker}'
        else:
            return render(request, 'inicio/crear_accion.html', {'formulario': formulario})

    formulario = CrearAccionFormulario()
    return render(request, 'inicio/crear_accion.html', {'formulario': formulario, 'mensaje': mensaje})


def crear_futuro(request):

    mensaje = ''
    if request.method == 'POST':
        formulario = CrearFuturoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            futuro = Futuro(ticker=info['ticker'], descripcion=info['descripcion'], fecha_vencimiento=info['fecha_vencimiento'])
            futuro.save()
            mensaje = f'Se creó el futuro {futuro.ticker}'
        else:
            return render(request, 'inicio/crear_futuro.html', {'formulario': formulario})

    formulario = CrearFuturoFormulario()
    return render(request, 'inicio/crear_futuro.html', {'formulario': formulario, 'mensaje': mensaje})