from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Ubicacion
from .models import Reporte


def home(request):
    return render(request, "home.html")


def reporte(request, id = None):
    if request.method == "POST":
        Reporte.objects.create(
            ubicacion=request.POST.get("ubicacion"),
            equipo=request.POST.get("equipo"),
            tipo=request.POST.get("incidencia"),
            rrhh=request.POST.get("usuario"),
            descripcion=request.POST.get("descripcion"),
        )
    context = {}
    if id is not None:
        p = Reporte.objects.get(id=id)
        context["post"] = p

    return render(request, "reporte.html", context)


def lista(request):
    incidentes = Reporte.objects.all()
    return render(request, "lista.html", {"incidentes": incidentes})
