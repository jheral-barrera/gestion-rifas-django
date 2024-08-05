from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
import random

from .forms import RifaForm, PremioForm, CompraForm, NumeroForm
from .models import Rifa, Premio, Numero, Compra

# Create your views here.
def rifas(req):
    rifas = Rifa.objects.all()

    datos = {
        'rifas': rifas
    }

    return render(req, 'rifas.html', datos)

def detalleRifa(req, id):
    rifa = Rifa.objects.get(id=id)
    premios = Premio.objects.filter(rifa=rifa)

    datos = {
        'rifa': rifa,
        'premios': premios,
    }

    return render(req, 'detalleRifa.html', datos)

def compraRifa(req, id):
    rifa = Rifa.objects.get(id=id)

    numeros_comprados = Numero.objects.filter(comprador__isnull=False, rifa=rifa).values_list('numero', flat=True)
    numeros_disponibles = range(1, int(rifa.cantidad_numeros_rifa) + 1)

    if req.method == 'POST':
        compra_form = CompraForm(req.POST)
        numero_form = NumeroForm(req.POST)

        if compra_form.is_valid():
            nombre_cliente = compra_form.cleaned_data['nombre_cliente']

            # REFACTORIZAR LAS VALIDACIONES - UTILIZAR LOS METODOS DEL CLEAN
            # Validacion para no registrar nombres iguales
            if Compra.objects.filter(nombre_cliente=nombre_cliente, rifa=rifa).exists():
                messages.error(req, 'El cliente ya se encuentra registrado en esta rifa')
                return redirect(f'/compraRifa/{id}')
        
            compra_form.save()
            messages.success(req, 'Cliente Registrado con exito :)')
            return redirect(f'/compraRifa/{id}')
        
        elif numero_form.is_valid():
            num_form = numero_form.save(commit=False)
            numero = numero_form.cleaned_data['numero']

            # REFACTORIZAR LAS VALIDACIONES - UTILIZAR LOS METODOS DEL CLEAN
            # Validacion para no comprar numeros iguales
            if Numero.objects.filter(numero=numero, rifa=rifa, comprador__isnull=False).exists():
                messages.error(req, "Este número ya ha sido comprado. Elige otro número.")
                return redirect(f'/compraRifa/{id}')
            if numero > rifa.cantidad_numeros_rifa:
                messages.error(req, "No es posible comprar ese numero :(")
                return redirect(f'/compraRifa/{id}')
            

            # Validacion del codigo
            # codigo_pago = numero_form.fields['codigo_pago'].initial
            codigo_pago = numero_form.cleaned_data['codigo_pago']

            try:
                numero_form.clean_codigo_pago()
                if 'codigo_pago' in req.POST and req.POST['codigo_pago']:
                    estado_comprado = 'Comprado'
                    num_form.estado_pago = estado_comprado
                else:
                    estado_reserveado = 'Reservado'
                    num_form.estado_pago = estado_reserveado
                messages.success(req, "El numero ha sido comprado con exito :)")
            except forms.ValidationError as e:
                messages.error(req, e.message)
                return redirect(f'/compraRifa/{id}')

            num_form.save()
            return redirect(f'/compraRifa/{id}')
        
    else:
        compra_form = CompraForm(initial={'rifa':rifa})
        numero_form = NumeroForm(initial={'rifa':rifa})

    datos = {
        'rifa': rifa,
        'compra_form': compra_form,
        'numero_form': numero_form,
        'numeros_disponibles': numeros_disponibles,
        'numeros_comprados': numeros_comprados
    }

    return render(req, 'compraRifa.html', datos)

def agregarRifa(req):
    rifas = Rifa.objects.all()
    rifa_form = RifaForm()

    datos = {
        'rifa_form': rifa_form,
        'rifas': rifas 
    }

    if req.method == 'POST':
        rifa_form = RifaForm(req.POST)
        if rifa_form.is_valid():
            rifa_form.save()
            messages.success(req, 'La rifa se agrego exitosamente :)')
            return redirect('/administrarRifas')
        else:
            messages.error(req, 'No se pudo registrar la rifa. Intente otra vez :(')
            return redirect('/administrarRifas')


    return render(req, 'adminRifas.html', datos)

def actualizarRifa(req, id):
    actualizando = 'actualizando'
    rifas = Rifa.objects.all()
    rifa = Rifa.objects.get(id=id)

    if req.method == 'POST':
        rifa_form = RifaForm(req.POST, instance=rifa)
        if rifa_form.is_valid():
            rifa_form.save()
            messages.success(req, 'Se actualizo correctamente :)')
            return redirect('/administrarRifas')
    else:
        rifa_form = RifaForm(instance=rifa)
    
    datos = {
        'rifa_form': rifa_form,
        'rifas': rifas,
        'actualizando': actualizando
    }

    return render(req, 'adminRifas.html', datos)

def eliminarRifa(req, id):
    rifa = Rifa.objects.get(id=id)
    rifa.delete()
    messages.success(req, 'Se ha eliminado correctamente :)')
    return redirect('/administrarRifas')

def agregarPremio(req):
    premios = Premio.objects.all()
    premio_form = PremioForm()

    datos = {
        'premio_form': premio_form,
        'premios': premios
    }

    if req.method == 'POST':
        premio_form = PremioForm(req.POST, req.FILES)
        if premio_form.is_valid():
            premio_form.save()
            messages.success(req, 'La rifa se agrego exitosamente :)')
            return redirect('/administrarPremios')
        else:
            messages.error(req, 'No se pudo registrar la rifa. Intente otra vez :(')
            return redirect('/administrarPremios')

    return render(req, 'adminPremios.html', datos)

def actualizarPremio(req, id):
    actualizando = 'actualizando'
    premios = Premio.objects.all()
    premio = Premio.objects.get(id=id)

    if req.method == 'POST':
        premio_form = PremioForm(req.POST, req.FILES, instance=premio)
        if premio_form.is_valid():
            premio_form.save()
            return redirect('/administrarPremios')
    else:
        premio_form = PremioForm(instance=premio)
    
    datos = {
        'premio_form': premio_form,
        'premios': premios,
        'actualizando': actualizando
    }

    return render(req, 'adminPremios.html', datos)

def eliminarPremio(req, id):
    premio = Premio.objects.get(id=id)
    premio.delete()
    return redirect('/administrarPremios')

def finalizarRifa(req, id):
    rifa = Rifa.objects.get(id=id)
    premios = Premio.objects.filter(rifa=rifa)

    numeros_comprados = list(Numero.objects.filter(comprador__isnull=False, rifa=rifa).values_list('numero', flat=True))
    print("numeros", numeros_comprados)

    ganador = random.sample(numeros_comprados, k=len(premios))
    print(ganador)

    for i, premio in enumerate(premios):
        numero_ganador = ganador[i]

        # Asociar el premio con el ganador
        premio.comprador = Numero.objects.get(numero=numero_ganador, rifa=rifa).comprador
        premio.save()

    rifa.estado_rifa = 'finalizada'
    rifa.save()

    datos = {
        'rifa': rifa,
        'premios': premios,
        'ganadores': ganador,
    }

    return render(req, 'ganadorRifa.html', datos)

def resultadosRifa(req, id):
    rifa = Rifa.objects.get(id=id)
    premios = Premio.objects.filter(rifa=rifa)

    numeros_comprados = list(Numero.objects.filter(comprador__isnull=False, rifa=rifa).values_list('numero', flat=True))
    print("numeros", numeros_comprados)

    datos = {
        'rifa': rifa,
        'premios': premios,
    }

    return render(req, 'ganadorRifa.html', datos)