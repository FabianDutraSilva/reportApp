from django.shortcuts import render

# Create your views here.

from .models import Reporte
from .models import Equipo

def home(request):
    """render home"""
    return render(request, "home.html")


def reporte(request, id = None):
    if request.method == "POST":
        id = request.POST.get('id')
        if id is None:
            Reporte.objects.create(
                ubicacion=request.POST.get("ubicacion"),
                equipo=request.POST.get("equipo"),
                tipo=request.POST.get("tipo"),
                rrhh=request.POST.get("rrhh"),
                descripcion=request.POST.get("descripcion"),
            )
        else:
            r = Reporte.objects.get(id = id)
            r.ubicacion = request.POST.get('ubicacion')
            r.equipo = request.POST.get('equipo')
            r.tipo = request.POST.get('tipo')
            r.rrhh = request.POST.get('rrhh')
            r.descripcion = request.POST.get('descripcion')
            r.save()

    context = {}
    if id is not None:
        r = Reporte.objects.get(id=id)
        context['reporte'] = r

    return render(request, "reporte.html", context)

def agregar_equipo(request, id = None):
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
        else:
            e = Equipo.objects.get(id = id)
            e.nombre = request.POST.get('nombre')
            e.marca = request.POST.get('marca')
            e.modelo = request.POST.get('modelo')
            e.serie = request.POST.get('serie')
            e.codigo= request.POST.get('codigo'),
            e.centroCosto = request.POST.get('centroCosto')
            e.prioridad = request.POST.get('prioridad')
            e.parteDe = request.POST.get('parteDe')
            e.save()

    context = {}
    if id is not None:
        e = Equipo.objects.get(id=id)
        context['equipo'] = e

    return render(request, "agregar-equipo.html", context)


def incidentes(request):
    lista_incidentes = Reporte.objects.all()
    return render(request, "incidentes.html", {"incidentes": lista_incidentes})

def equipos(request):
    lista_equipos = Equipo.objects.all()
    return render(request, "equipos.html", {"equipos": lista_equipos})