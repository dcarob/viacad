from django.contrib import admin
from .models import Profesores
from .models import Materias
from .models import Alumnos
from .models import Solicitud

admin.site.register(Profesores)
admin.site.register(Materias)
admin.site.register(Alumnos)
admin.site.register(Solicitud)

# Register your models here.
