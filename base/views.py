from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

# Create your views here.

from .models import Reporte
from .models import Equipo

def home(request):
    return render(request, "home.html")

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')

        messages.error(request, 'Usuario y/o contraseña incorrectos')

    return render(request, "login.html")

def logoutPage(request):
    logout(request)
    return redirect('/')

def registro(request):
    if (request.method == 'POST'):
        firstName = request.POST.get('first-name')
        lastName = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ingresado ya existe')
            return redirect('/registro')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El email ingresado ya existe')
            return redirect('/registro')
        else:
            User.objects.create_user(username, email=email, password=password, first_name=firstName, last_name=lastName)
            return redirect('../login')
    return render(request, "registro.html")

def reporte(request, id = None):
    if request.method == "POST":
        id = request.POST.get('id')
        if id is None:
            Reporte.objects.create(
                ubicacion=request.POST.get("ubicacion"),
                equipo=request.POST.get("equipo"),
                titulo=request.POST.get("titulo"),
                tipo=request.POST.get("tipo"),
                descripcion=request.POST.get("descripcion"),
                user=request.user
            )
            messages.success(request, 'Incidente reportado correctamente')
            return redirect('../reportes')
        else:
            r = Reporte.objects.get(id = id)
            r.ubicacion = request.POST.get('ubicacion')
            r.equipo = request.POST.get('equipo')
            r.titulo = request.POST.get('titulo')
            r.tipo = request.POST.get('tipo')
            r.descripcion = request.POST.get('descripcion')
            r.save()

            messages.success(request, 'Incidente actualizado correctamente')
            return redirect('../reportes')

    context = {}
    if id is not None:
        r = Reporte.objects.get(id=id)
        context['reporte'] = r

    return render(request, "reporte.html", context)

def equipo(request, id = None):
    if request.method == "POST":
        id = request.POST.get('id')
        if id is None:
            Equipo.objects.create(
                nombre=request.POST.get("nombre"),
                marca=request.POST.get("marca"),
                modelo=request.POST.get("modelo"),
                serie=request.POST.get("serie"),
                codigo=request.POST.get("codigo"),
                centroCosto=request.POST.get("centroCosto"),
                prioridad=request.POST.get("prioridad"),
                parteDe=request.POST.get("parteDe")
            )
            messages.success(request, 'Equipo creado correctamente')
            return redirect('../equipos')
        else:
            e = Equipo.objects.get(id = id)
            e.nombre = request.POST.get('nombre')
            e.marca = request.POST.get('marca')
            e.modelo = request.POST.get('modelo')
            e.serie = request.POST.get('serie')
            e.codigo= request.POST.get('codigo')
            e.centroCosto = request.POST.get('centroCosto')
            e.prioridad = request.POST.get('prioridad')
            e.parteDe = request.POST.get('parteDe')
            e.save()

            messages.success(request, 'Equipo actualizado correctamente')
            return redirect('../equipos')
    context = {}
    if id is not None:
        e = Equipo.objects.get(id=id)
        context['equipo'] = e

    return render(request, "equipo.html", context)

def reportes(request):
    lista_incidentes = Reporte.objects.order_by('-created')
    return render(request, "reportes.html", {"incidentes": lista_incidentes})

def equipos(request):
    lista_equipos = Equipo.objects.order_by('-created')
    return render(request, "equipos.html", {"equipos": lista_equipos})

def confirmar_borrar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, "confirmar_borrar_equipo.html", {"equipo": equipo})

def confirmar_borrar_reporte(request, id):
    reporte = Reporte.objects.get(id=id)
    return render(request, "confirmar_borrar_reporte.html", {"reporte": reporte})

def borrar_reporte(request, id):
    reporte = Reporte.objects.get(id=id)
    reporte.delete()
    messages.success(request, 'Reporte eliminado correctamente')
    return HttpResponseRedirect('../reportes')

def borrar_equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo.delete()
    messages.success(request, 'Equipo eliminado correctamente')
    return HttpResponseRedirect('../equipos')