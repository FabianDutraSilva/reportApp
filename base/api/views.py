from django.http import JsonResponse
from ..models import Reporte

def routes(request):
    routes = [
        'GET /api/reportes',
        'GET /api/reporte/:id'
    ]
    return JsonResponse(routes, safe=False)

def reportes(request):
    reportes = Reporte.objects.all()
    reportes_dict = []
    for r in reportes:
        reportes_dict.append({
            'titulo': r.titulo,
            'equipo': r.equipo,
            'descripcion': r.descripcion
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