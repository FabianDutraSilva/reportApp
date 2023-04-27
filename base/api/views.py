from django.http import JsonResponse
from ..models import Reporte
from ..models import Equipo

def routes(request):
    routes = [
        'GET /api/reportes',
        'GET /api/reporte/:id',
        'GET /api/equipos',
        'GET /api/equipo/:id'
    ]
    return JsonResponse(routes, safe=False)

def reportes(request):
    reportes = Reporte.objects.all()
    reportes_dict = []
    for r in reportes:
        reportes_dict.append({
            'titulo': r.titulo,
            'equipo': r.equipo,
            'descripcion': r.descripcion,
            'id': r.id
        })
    return JsonResponse(reportes_dict, safe=False)

def reporte(request, id):
    reporte = Reporte.objects.get(id=id)
    reporte_dict={
        'titulo': reporte.titulo,
        'equipo': reporte.equipo,
        'descripcion': reporte.descripcion,
        'id': reporte.id
    }
    return JsonResponse(reporte_dict, safe=False)

def equipos(request):
    equipos = Equipo.objects.all()
    equipos_dict = []
    for e in equipos:
        equipos_dict.append({
            'nombre': e.nombre,
            'marca': e.marca,
            'modelo': e.modelo,
            'serie': e.serie,
            'codigo': e.codigo,
            'id': e.id
        })
    return JsonResponse(equipos_dict, safe=False)

def equipo(request, id):
    equipo = Equipo.objects.get(id=id)
    equipo_dict={
        'nombre': equipo.nombre,
        'marca': equipo.marca,
        'modelo': equipo.modelo,
        'serie': equipo.serie,
        'codigo': equipo.codigo,
        'id': equipo.id
    }
    return JsonResponse(equipo_dict, safe=False)