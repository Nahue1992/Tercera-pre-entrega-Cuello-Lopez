from django.shortcuts import render, redirect
from inicio.forms import CrearAccionFormulario, CrearBonoFormulario, CrearFuturoFormulario, BuscarEspeciesFormulario
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
            return redirect('inicio:listar_especies')
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
            return redirect('inicio:listar_especies')
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
            return redirect('inicio:listar_especies')
        else:
            return render(request, 'inicio/crear_futuro.html', {'formulario': formulario})

    formulario = CrearFuturoFormulario()
    return render(request, 'inicio/crear_futuro.html', {'formulario': formulario, 'mensaje': mensaje})

def listar_especies(request):

    formulario = BuscarEspeciesFormulario(request.GET)
    ticker_a_buscar = None
    if formulario.is_valid():
        ticker_a_buscar = formulario.cleaned_data['ticker']
        listado_de_bonos = Bono.objects.filter(ticker__icontains=ticker_a_buscar)
        listado_de_acciones = Accion.objects.filter(ticker__icontains=ticker_a_buscar)
        listado_de_futuros = Futuro.objects.filter(ticker__icontains=ticker_a_buscar)
    formulario = BuscarEspeciesFormulario()
    return render(request, 'inicio/listar_especies.html', {'formulario': formulario, 'Bonos': listado_de_bonos,
                                                           'Acciones': listado_de_acciones,'Futuros': listado_de_futuros})

#