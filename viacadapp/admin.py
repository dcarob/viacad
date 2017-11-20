from django.contrib import admin
from .models import Profesores
from .models import Materias
from .models import Alumnos
from .models import Solicitud
from .models import Votaciones

admin.site.register(Profesores)
admin.site.register(Materias)
admin.site.register(Alumnos)
admin.site.register(Solicitud)
admin.site.register(Votaciones)

# Register your models here.
