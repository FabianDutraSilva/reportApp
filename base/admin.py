from django.contrib import admin

# Register your models here.

from .models import Ubicacion
from .models import Equipo
from .models import Rrhh
from .models import Causa
from .models import Tipo
from .models import Reporte

admin.site.register(Ubicacion)
admin.site.register(Equipo)
admin.site.register(Rrhh)
admin.site.register(Causa)
admin.site.register(Tipo)
admin.site.register(Reporte)
